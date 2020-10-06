"""Users urls"""

#Django
from django.urls import path

#views
from cride.users.views import UserLoginApiView

urlpatterns = [
    path('users/login',UserLoginApiView.as_view(),name='login')
]
