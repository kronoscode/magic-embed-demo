# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.forms import ModelForm

# Create your models here.

class magic(models.Model):
    """docstring for ClassName"""

    titulo = models.CharField(max_length=50, blank=True)
    url = models.URLField(blank=True)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"

class MagicForm(ModelForm):
 
    class Meta:
        model = magic