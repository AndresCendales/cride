""" Admin for Circles app """

#Django 
from django.contrib import admin

#Models
from cride.circles.models import Circle, Membership, Invitation

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

    actions = ['make_verified','make_unverified']

    def make_verified(self,request, queryset):
        """Make circles verified"""
        queryset.update(verified=True)
    make_verified.short_description = 'Make selected circles verified'

    def make_unverified(self,request, queryset):
        """Make circles verified"""
        queryset.update(verified=False)
    make_unverified.short_description = 'Make selected circles unverified'

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
@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    """Invitation Admin"""

    list_display = (
        'code',
        'issued_by',
        'circle',
        'used',
        'used_at',
    )

    list_filter = (
        'code',
        'issued_by',
        'circle',
        'used',
        'used_at',
    )

