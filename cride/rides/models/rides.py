""" Rides Models """

# Django
from django.db import models

# Utils
from cride.utils.models import CRideModel
from datetime import datetime


class Ride(CRideModel):
    """ Ride Model """

    offered_by = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True
        )
    
    offered_in = models.ForeignKey(
        "circles.Circle",
        on_delete=models.SET_NULL,
        null=True
        )
    passengers = models.ManyToManyField(
        "users.User", 
        related_name='passengers',
        )
    avaliable_seats = models.PositiveSmallIntegerField(
        default=1
        )
    comments = models.TextField(
        blank=True,
        )
    departure_location = models.CharField(
        max_length=255
        )
    departure_date = models.DateTimeField()
    arrival_location = models.CharField(
        max_length=255
        )
    arrival_date = models.DateTimeField()
    rating = models.FloatField(
        null=True
        )
    is_active = models.BooleanField(
        'active status',
        default=False,
        help_text='Used for disabling the ride or marking it has finished'
        )

    class Meta:
        verbose_name = "Ride"
        verbose_name_plural = "Rides"
    
    def __str__(self):
        return '{_from} to {to} | {day} {i_time} - {f_time}'.format(
            _from=self.departure_location,
            to=self.arrival_location,
            day=self.departure_date.strftime('%a %d, %b'),
            i_time=self.departure_date.strftime('%I:%M %p'),
            f_time=self.arrival_date.strftime('%I:%M %p'),
        )