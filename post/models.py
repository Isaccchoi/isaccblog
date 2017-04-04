from django.db import models
from django.shortcuts import reverse
from django.conf import settings

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


PERMISSIBLE_RANGE_CHOICE = (
    ("onlyme", "나에게만"),
    ("friends", "친구만"),
    ("public", "모두에게"),
)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=120)
    content = models.TextField()
    tags = models.ManyToManyField("tag")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    # permissbile_range = models.CharField(max_length=120,
                            # choice=PERMISSIBLE_RANGE_CHOICE)
    # image
    class Meta:
        ordering = ["-updated_at",]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"post_id": self.pk})


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False)
    post = models.ForeignKey(Post)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at",]


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
