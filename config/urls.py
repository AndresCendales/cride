"""Main URLs module."""

from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),

    #Circles
    path('',include(('cride.circles.urls','circles'),namespace='circles')),
    
    #Users
    path('',include(('cride.users.urls','users'),namespace='users')),

    #Rides
    path('',include(('cride.rides.urls','rides'),namespace='rides')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
