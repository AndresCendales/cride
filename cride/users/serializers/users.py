"""Users Serializers """
#Django
from django.contrib.auth import authenticate, password_validation
from django.core.validators import RegexValidator

# Django Resto Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

#Models
from cride.users.models import User, Profile

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


class UserSignUpSerializer(serializers.Serializer):
    """User SignUp Serializer.

    Handle the signup request data validation and profile/user creation.
    """

    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    username = serializers.CharField(
        min_length = 4,
        max_length = 20,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    #Phone Number
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )

    phone_number = serializers.CharField(
        validators=[phone_regex],
    )

    #password
    password = serializers.CharField(
        min_length = 8,
        max_length = 64,
    )
    password_confirmation = serializers.CharField(
        min_length = 8,
        max_length = 64,
    )

    #Name
    first_name = serializers.CharField(
        min_length = 2,
        max_length = 30,
    )
    last_name = serializers.CharField(
        min_length = 2,
        max_length = 30,
    )

    def validate(self, data):
        """Verifi passwords match"""
        passwd = data['password']
        passwd_confirmation = data['password_confirmation']

        if passwd != passwd_confirmation:
            raise serializers.ValidationError("Passwords don't match.")
        password_validation.validate_password(passwd)

        return data

    def create(self, validated_data):
        """Handle user and profile creation"""
        validated_data.pop('password_confirmation')
        user = User.objects.create_user(**validated_data)
        profile = Profile.objects.create(user=user)
        return user

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