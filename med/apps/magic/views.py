# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import DetailView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import Video
from .forms import VideoForm


class VideoView(DetailView):
    model = Video
    template_name = 'magic/video_detail.html'
    context_object_name = "video"

def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            new_video = form.save()

            return HttpResponseRedirect(reverse('magic:video_detail', args=(new_video.pk,)))
    else:
        form = VideoForm()

    return render(request, 'index.html', {'form': form})
