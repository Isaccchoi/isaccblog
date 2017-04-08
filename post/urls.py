from django.conf.urls import url
from django.contrib import admin

from .views import PostCreateView
from .views import PostDetailView
from .views import PostUpdateView
from .views import PostDeleteView
from .views import CommentDeleteView
from .views import CommentUpdateView


urlpatterns = [
    url(r'^create/$', PostCreateView.as_view(), name="create"),
    url(r'^(?P<post_id>\d+)/$', PostDetailView.as_view(), name="detail"),
    url(r'^(?P<post_id>\d+)/update/$', PostUpdateView.as_view(), name="update"),
    url(r'^(?P<post_id>\d+)/delete/$', PostDeleteView.as_view(), name="delete"),
    url(r'^(?P<comment_id>\d+)/delete_comment/$', CommentDeleteView.as_view(),\
                                                        name="delete_comment"),
    url(r'^(?P<comment_id>\d+)/update_comment/$', CommentUpdateView.as_view(),\
                                                        name="update_comment"),
]
