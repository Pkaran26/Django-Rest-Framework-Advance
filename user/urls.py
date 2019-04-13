from django.urls import path
from .views import *

urlpatterns = [
    path('createuser/', CreateUser.as_view()),
    path('profile/<int:pk>', UserProfile.as_view())
]
