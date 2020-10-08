""" Cricle seriallizers """

# Django Rest Framework
from rest_framework import serializers

# Model 
from cride.circles.models import Circle

class CircleModelSerializer(serializers.ModelSerializer):
    """Circle Model Serializer"""

    class Meta:
        """Meta Class."""

        model =Circle
        fieldds = (
            'id',
            'name',
            'slug_name',
            'about',
            'picture'
            'riddes_offered',
            'rides_taken',
            'verified',
            'is_public',
            'is_limited',
            'members_limit'
        )