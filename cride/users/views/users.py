"""" Users views """

#Django Rest Framework
from rest_framework.views import  APIView
from rest_framework import status

#Serializer
from cride.users.serializers import UserLoginSerializer

class UserLoginApiView(APIView):
    """User Login API View """
    def post(self,request, *args, **kwargs):
        """Handle http Post Request"""

        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = serializer.save()

        data = {
            'status':'ok',
            'token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)