from rest_framework import serializers
from .models import *
from user.serializers import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        depth = 1
        fields = ('id', 'user', 'comment', 'createdAt')

class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    comments = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Article
        depth = 2
        fields = ('user', 'category', 'title', 'body', 'createdAt', 'comments')

    def to_representation(self, instance):
        comments = []
        for c in instance.comments.all():
            comment = {
                "id": c.id,
                "user": c.user.username,
                "user_id": c.user.id,
                "comment": c.comment,
                "createdAt": c.createdAt
            }
            comments.append(comment)
        data = {
          "title": instance.title,
          "body": instance.body,
          "createdAt": instance.createdAt,
          "user_id": instance.user.id,
          "username": instance.user.username,
          "category_id": instance.category.id,
          "categoryName": instance.category.name,
          "first_name": instance.user.first_name,
          "last_name": instance.user.last_name,
          "comments": comments
        }
        return data



class HomeSerializers(serializers.Serializer):
    def to_representation(self, instance):
        article = ArticleSerializer(instance['article'], many=True)
        category = CategorySerializer(instance['category'], many=True)
        user = UserSerializer(instance['user'], many=True)

        data = {
          "article": article.data,
          "category": category.data,
          "user": user.data
        }
        return data
