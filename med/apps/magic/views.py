# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import DetailView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import Magic, MagicForm


class VideoView(DetailView):
    model = Magic
    template_name = 'magic/video_detail.html'
    context_object_name = "video"

def add_video(request):
    if request.method == 'POST':
        form = MagicForm(request.POST) 
        if form.is_valid():
            new_magic = form.save() 

            return HttpResponseRedirect(reverse('magic:list_video', args=(new_magic.pk,)))
    else:
        form = MagicForm() 
 
    return render(request, 'index.html', {'form': form})