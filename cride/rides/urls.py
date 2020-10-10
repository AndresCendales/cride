"""Rides urls"""

#Django
from django.urls import path, include

# Django Rest Framework 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('',include(router.urls))
]