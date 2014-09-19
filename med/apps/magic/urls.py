from django.conf.urls import patterns, url

from .views import VideoView

urlpatterns = patterns('magic.views',
    url(r'^video/(?P<pk>\d+)/$', VideoView.as_view(), name='video_detail'),
    url(r'^$', 'add_video', name='add_video'),
)
