"""Users Serializers """
#Django
from django.contrib.auth import authenticate

# Django Resto Framework
from rest_framework import serializers

#Models
from rest_framework.authtoken.models import Token
from cride.users.models import User

class UserModelSerializer(serializers.ModelSerializer):
    """User Model Serializer"""

    class Meta: 
        """Meta Class."""
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'phone_number'
        )

class UserLoginSerializer(serializers.Serializer):
    """User Login Serializer.

    Handle the login request data
    
    """
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8,max_length=64)

    def validate(self, data):
        """Check credentials """

        user = authenticate(username=data['email'],password=data['password'])
        
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        
        self.context['user'] = user
        return data
    
    def create(self,data):
        """Generate or retrieve new token """
        token , created = Token.objects.get_or_create(user=self.context['user'])

        return self.context['user'], token.key