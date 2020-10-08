"""Circles Views"""

# Django Rest Framework
from rest_framework import viewsets

# Models
from cride.circles.models import Circle

# Serializer
from cride.circles.serializers.circles import CircleModelSerializer 

class CircleViewSet(viewsets.ModelViewSet):
    """Circle viewset. """

    queryset = Circle.objects.all()
    serializer_class = CircleModelSerializer