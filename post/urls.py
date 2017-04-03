from django.conf.urls import url
from django.contrib import admin

from .views import PostList


urlpatterns = [
    url(r'^list/$', PostList.as_view(), name="list"),
]
