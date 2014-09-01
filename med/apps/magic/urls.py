from django.conf.urls import patterns
from django.conf.urls import url
 
from . import views
 
urlpatterns = patterns('',
    url(r'^$(\d+)/list/$', views.VideoList.as_view(), name='list_video'),
    url(r'^$', views.add_video, name='add_video'),
)