# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import magic, MagicForm


class VideoView(ListView):
 
    model = magic
    template_name = 'magic/video_list.html'

def add_video(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = MagicForm(request.POST) # Bound form
        if form.is_valid():
            new_magic = form.save() # Guardar los datos en la base de datos
 
            return HttpResponseRedirect(reverse('magic:list_video'))
    else:
        form = MagicForm() # Unbound form
 
    return render(request, 'index.html', {'form': form})