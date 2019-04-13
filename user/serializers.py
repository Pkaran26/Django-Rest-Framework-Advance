from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset = User.objects.all())
    username = serializers.StringRelatedField(source='user_id',read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'
