"""" users Models"""

from django.db import models
from django.contrib.auth.models import AbstractUser

#utilities
from cride.utils.models import CRideModel

class User(CRideModel, AbstractUser):
    """ User Model

    Extend from django's abstract user, change the username field to email
    and some extra fields"""

    email = models.EmailField(
        'email address', 
        unique=True,
        error_message={
            'unique':'A user with that email already exists.'
        }
        max_length=254
    )

    phone = models.CharField(
        max_length=17,
        blank=True
    )

    USENAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name','last_name']

    is_client = models.BooleanField(
        'client_status',
        default=True,
        help_text = (
        'Help easily distinguish users and perform queries.'
        'Clients are the main type of user'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default = False,
        help_text='Set to true when the user have verified its email address'
    )