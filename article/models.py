from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    body = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Reached(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    reach = models.CharField(max_length=5)

    def __str__(self):
        return self.reach

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
