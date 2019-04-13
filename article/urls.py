from django.urls import path
from .views import *

urlpatterns = [
    path('home/', Home.as_view()),
    path('articles/', Articles.as_view()),
]
