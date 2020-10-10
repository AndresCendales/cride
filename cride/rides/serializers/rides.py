"""Rides Serializer """

# Django Rest framework
from rest_framework import serializers

# Models
from cride.rides.models import Ride

# Utilities 
from datetime import timedelta
from django.utils import timezone
class CreateRideSerializer(serializers.ModelField):
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
