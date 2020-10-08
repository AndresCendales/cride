"""Circles Views"""

# Django Rest Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Models
from cride.circles.models import Circle

# Serializer
from cride.circles.serializers.circles import CircleModelSerializer 

class CircleViewSet(viewsets.ModelViewSet):
    """Circle viewset. """


    serializer_class = CircleModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Restrict list to public-only"""
        queryset = Circle.objects.all()
        if self.action == 'list':
            return queryset.filter(is_public=True)
        return queryset
    