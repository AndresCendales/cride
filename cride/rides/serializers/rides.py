"""Rides Serializer """

# Django Rest framework
from rest_framework import serializers

# Models
from cride.rides.models import Ride
from cride.circles.models import Membership

# Utilities 
from datetime import timedelta
from django.utils import timezone


class CreateRideSerializer(serializers.ModelSerializer):
    """ Create ride serializer """

    offered_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    avaliable_seats = serializers.IntegerField(min_value=1,max_value=15)
    
    class Meta:
        """Meta Class """
        model = Ride
        exclude = (
            'passengers',
            'rating',
            'is_active',
            'offered_in',
        )

    def validate_departure_date(self,data):
        """Verify departure date is not in the past"""
        min_date = timezone.now()+ timedelta(minutes=10)

        if data < min_date:
            raise serializers.ValidationError(
                    'Departure time must be at least pass the next 10 minutes window'
                )
        return data

    def validate(self,data):
        """Validate.

        Verify that the person who offers the ride is memb
        and also the same user making the request.
        """
        if self.context['request'].user != data['offered_by']:
            raise serializers.ValidationError('Rides Offered on behalf of others are not allowed')
        
        user = data['offered_by']
        circle =  self.context['circle']
        
        try:
            membership = Membership.objects.get(
                user=user, 
                circle=circle, 
                is_active=True
            )
        except  Membership.DoesNotExist:
            raise serializers.ValidationError('User is not an active member of the circle.')
        
        if data['arrival_date'] <= data['departure_date']:
            raise serializers.ValidationError('Departure must be happen after arrival date.')
        
        self.context['membership']= membership
        return data

def create(self, data):
        """Create ride and update stats."""
        circle = self.context['circle']
        ride = Ride.objects.create(**data, offered_in=circle)

        # Circle
        circle.rides_offered += 1
        circle.save()

        # Membership
        membership = self.context['membership']
        membership.rides_offered += 1
        membership.save()

        # Profile
        profile = data['offered_by'].profile
        profile.rides_offered += 1
        profile.save()

        return ride