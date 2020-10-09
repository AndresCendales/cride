"""Circles Views"""

# Django Rest Framework
from rest_framework import viewsets, mixins

#Permissions
from rest_framework.permissions import IsAuthenticated
from cride.circles.permissions import IsCircleAdmin

# Models
from cride.circles.models import Circle, Membership

# Serializer
from cride.circles.serializers.circles import CircleModelSerializer 

class CircleViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Circle viewset. """


    serializer_class = CircleModelSerializer

    def get_permissions(self):
        """Assign permissions based on actions."""
        permissions = [IsAuthenticated]
        if self.action in ['update','partial_update']:
            permissions.append(IsCircleAdmin)
        return [permission() for permission in permissions]


    def get_queryset(self):
        """Restrict list to public-only"""
        queryset = Circle.objects.all()
        if self.action == 'list':
            return queryset.filter(is_public=True)
        return queryset
    
    def perform_create(self, serializer):
        """ Asigned circle admin member"""
        circle = serializer.save()
        user = self.request.user
        profile = user.profile
        Membership.objects.create(
            user=user,
            profile=profile,
            circle=circle,
            is_admin=True,
            remaining_invitations=10
        )