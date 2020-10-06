"""" Users views """

#Django Rest Framework
from rest_framework.views import  APIView
from rest_framework import status
from rest_framework.response import Response

#Serializer
from cride.users.serializers import (
        UserLoginSerializer, UserModelSerializer
    )
class UserLoginApiView(APIView):
    """User Login API View """
    def post(self,request, *args, **kwargs):
        """Handle http Post Request"""

        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user, token = serializer.save()

        data = {
            'user':UserModelSerializer(user).data,
            'acces_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
    
