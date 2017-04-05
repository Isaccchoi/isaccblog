from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


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

    def form_valid(self, form, *args, **kwargs):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(PostCreateView, self).form_valid(form, *args, **kwargs)



class PostDetailView(DetailView):
    context_object_name = "post"
    model = Post
    template_name = "post/detail.html"

    def get_object(self, *args, **kwargs):
        post_id = self.kwargs.get("post_id")
        return Post.objects.get(id=post_id)



class PostUpdateView(UpdateView):
    model = Post
    fields = ("category", "title", "content", "tags", "active", )
    template_name = "post/update.html"

    def get_object(self, *args, **kwargs):
        post_id = self.kwargs.get("post_id")
        return Post.objects.get(id=post_id)



class PostDeleteView(DeleteView):
    model = Post
    template_name = "post/delete.html"
    context_object = "post"

    def get_success_url(self, *args, **kwargs):
        return reverse("list")

    def get_object(self, *args, **kwargs):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        if post.user != self.request.user:
            raise Http404
        return post
