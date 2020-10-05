""" Circles Views """

#Django Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

#Models
from cride.circles.models import Circle

#Serializer 
from cride.circles.serializers import CircleSerializer, CreateCircleSerializer

@api_view(['GET'])
def list_circles(request):
    """List Circles. """

    return Response('Hola')

@api_view(['POST'])
def create_circle(request):
    """Create Circle"""
    
    serializer = CreateCircleSerializer(request.data)
    serializer.is_valid(raise_exception=True)
    circle = serializer.save()
    return Response(circle)