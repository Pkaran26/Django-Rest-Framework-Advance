from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from user.models import *
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.response import Response

class Home(generics.ListAPIView):
    article = Article.objects.all()
    category = Category.objects.all()
    user = User.objects.all()
    obj = {
        "article": article,
        "category": category,
        "user": user
    }
    queryset = [obj]
    serializer_class = HomeSerializers

class Articles(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
