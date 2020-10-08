"""Users urls"""

#Django
from django.urls import path

#views
from cride.users.views import (
    UserLoginApiView, 
    UserSignUpApiView, 
    AccountVerificationApiView
    )

urlpatterns = [
    path('users/login',UserLoginApiView.as_view(),name='login'),
    path('users/signup',UserSignUpApiView.as_view(),name='signup'),
    path('users/verify',AccountVerificationApiView.as_view(),name='verify'),
    
]
