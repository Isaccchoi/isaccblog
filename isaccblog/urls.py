from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login_page',),
    url(r'^logout/$', logout, {'next_page': settings.LOGIN_URL}),
    url(r'^post/', include('post.urls'), name="post"),
    url(r'^admin/', admin.site.urls),
]
