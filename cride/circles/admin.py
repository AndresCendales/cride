""" Admin for Cicles app """

#Django 
from django.contrib import admin

#Models
from cride.circles.models import Circle, Membership

@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    """Circle  admin."""

    list_display = (
        'slug_name',
        'name',
        'is_public',
        'verified',
        'is_limited',
        'members_limit',
    )

    search_fields = (
        'slug_name',
        'name',
    )

    list_filter = (
        'is_public',
        'verified',
        'is_limited',
    )

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    """Membership  admin."""

    list_display = (
        'user',
        'profile',
        'circle',
        'is_admin',
        'used_invitations',
        'remaining_invitations',
        'invited_by',
    )

    search_fields = (
        'user',
        'circle',
    )

    list_filter = (
        'user',
        'circle',
    )