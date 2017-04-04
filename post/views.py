from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView


# Create your views here.

from .models import Post
from .forms import PostForm

class PostList(ListView):
    context_object_name = "posts"
    template_name = "post/list.html"

    def get_queryset(self):
        post = Post.objects.all().filter(active=True)
        return post


class PostCreateView(CreateView):
    form_class = PostForm
    template_name = "post/create.html"


    def get_success_url(self, *args, **kwargs):
        return reverse("list")
