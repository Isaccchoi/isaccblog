from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView


# Create your views here.

from .models import Post
from .models import Tag
from .models import Comment
from .forms import PostForm
from .forms import CommentForm

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
        return reverse("home")

    def form_valid(self, form, *args, **kwargs):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        mass_tags = form.cleaned_data.get('tags', '')
        tags = mass_tags.split(",")
        for _tag in tags:
            _tag = _tag.strip()
            tag, _ = Tag.objects.get_or_create(name=_tag)
            post.tags.add(tag)
        return super(PostCreateView, self).form_valid(form, *args, **kwargs)



class PostDetailView(DetailView, FormView):
    # context_object_name = "post"
    form_class= CommentForm
    model = Post
    template_name = "post/detail.html"

    def get_object(self, *args, **kwargs):
        post_id = self.kwargs.get("post_id")
        return Post.objects.get(id=post_id)

    def get_context_data(self, *args, **kwargs):
        post = super(PostDetailView, self).get_context_data(*args, **kwargs)
        specific_post = Post.objects.get(id=self.kwargs.get("post_id"))
        comments = Comment.objects.filter(post=specific_post)
        if comments:
            post["comments"] = comments
        if self.request.user.is_authenticated():
            post["comment_authenticate"] = True
            post["post_authenticate"] = True
        # fixme - if user is this postowner or staff, can handle this
        return post

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)

        if form.is_valid():
            post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
        return FormView.post(self, request, *args, **kwargs)


    def get_success_url(self, *args, **kwargs):
        return reverse("detail", kwargs={"post_id":self.kwargs.get("post_id")})



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
        return reverse("home")

    def get_object(self, *args, **kwargs):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        if post.user != self.request.user:
            raise Http404
        return post



class CommentDeleteView(DeleteView):
    model = Comment
    template_name = "post/delete_comment.html"
    context_object = "comment"

    def get_success_url(self, *args, **kwargs):
        return reverse("detail", kwargs={"post_id":self.request.session["post_id"]})


    def get_object(self, *args, **kwargs):
        comment_id = self.kwargs.get("comment_id")
        comment = get_object_or_404(Comment, id=comment_id)
        self.request.session["post_id"] = comment.post.id
        return comment
