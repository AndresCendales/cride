"""Membership model"""

# Django 
from django.db import models

# Utilities
from cride.utils.models import CRideModel

# Moodels
from cride.users.models import users


class Membership(CRideModel):
    """Membership Model

    A membership is the table that holds the relationship
    beetween a user and a circle.
    """

    user = models.ForeignKey("users.User", verbose_name="User", on_delete=models.CASCADE)
    profile = models.ForeignKey("users.Profile", verbose_name="Profile", on_delete=models.CASCADE)
    circle = models.ForeignKey("circles.Circle", verbose_name="Circle", on_delete=models.CASCADE)
    
    is_admin =   models.BooleanField(
        'circle admin',
        default=False,
        help_text='Circcle admins can update the circles data and manage its members'
    )

    # Invitations
    used_invitations = models.PositiveSmallIntegerField(default=0)
    remaining_invitations = models.PositiveSmallIntegerField(default=0)
    invited_by = models.ForeignKey(
        "users.User", 
        null=True,
        on_delete=models.SET_NULL,
        related_name='invited_by',
    )

    # stats
    rides_taken = models.PositiveIntegerField(default=0)
    rides_offered = models.PositiveIntegerField(default=0)

    # Status
    is_active = models.BooleanField(
        'active status',
        default=True,
        help_text='Only  ative users are allowed to interacct in the circle'
    )

    def __str__(self):
        """  Return username and circle."""
        return  '@{} at #{}'.format(self.user.username,self.circle.slug_name)
