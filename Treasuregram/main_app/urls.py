from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^([0-9]+)/$', views.detail),
    url(r'^post_url/$', views.post_treasure),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT,}),
    ]
