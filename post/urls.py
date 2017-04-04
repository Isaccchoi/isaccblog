from django.conf.urls import url
from django.contrib import admin

from .views import PostList
from .views import PostCreateView
from .views import PostDetailView
from .views import PostUpdateView


urlpatterns = [
    url(r'^$', PostList.as_view(), name="list"),
    url(r'^create/$', PostCreateView.as_view(), name="create"),
    url(r'^(?P<post_id>\d+)/$', PostDetailView.as_view(), name="detail"),
    url(r'^(?P<post_id>\d+)/update/$', PostUpdateView.as_view(), name="update"),
]
