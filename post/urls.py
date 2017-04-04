from django.conf.urls import url
from django.contrib import admin

from .views import PostList
from .views import PostCreateView
from .views import PostDetailView


urlpatterns = [
    url(r'^list/$', PostList.as_view(), name="list"),
    url(r'^create/$', PostCreateView.as_view(), name="create"),
    url(r'^detail/(?P<post_id>\d+)/$', PostDetailView.as_view(), name="detail")
]
