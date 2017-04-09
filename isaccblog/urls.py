from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from post.views import PostListView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name="home"),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login',),
    url(r'^logout/$', logout, {'next_page': settings.LOGIN_URL}, name='logout'),
    url(r'^post/', include('post.urls'), name="post"),
    url(r'^admin/', admin.site.urls),
]

urlpatterns.append(
    url(r'',include('social.apps.django_app.urls', namespace='social'))
)


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
