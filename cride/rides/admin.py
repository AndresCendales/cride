""" Admin for Circles app """

#Django 
from django.contrib import admin

#Models
from cride.rides.models import Ride

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    """Ride  admin."""

    list_display = (
        'offered_by',
        'avaliable_seats',
        'comments',
        'departure_location',
        'departure_date',
        'arrival_location',
        'arrival_date',
        'rating',
        'is_active'
    )

    search_fields = (
        'offered_by',
        'offered_in',
        'passengers',
        'avaliable_seats',
        'departure_date',
        'arrival_date',
        'rating',
        'is_active'
    )

    list_filter = (
        'offered_by',
        'avaliable_seats',
        'departure_date',
        'arrival_date',
        'rating',
        'is_active'
        )