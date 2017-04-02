from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=120)
    content = models.TextField()
    tags = models.ManyToManyField('tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # image
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_at',]


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False)
    post = models.ForeignKey(Post)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at',]


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
