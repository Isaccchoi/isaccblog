from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.

from .models import Post

class PostList(ListView):
    model = Post
    template_name = "post/list.html"
    queryset = Post.objects.all()
