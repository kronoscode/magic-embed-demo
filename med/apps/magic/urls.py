from django.conf.urls import patterns, url

from . import views 
from .views import VideoView, add_video


urlpatterns = patterns('magic.views',
    url(r'^$', views.add_video, name='add_video'),
    url(r'^/list/$', VideoView.as_view(), name='list_video'),
)
