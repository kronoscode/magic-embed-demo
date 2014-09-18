# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.forms import ModelForm

# Create your models here.

class Magic(models.Model):
    """magic model"""

    TITLE = models.CharField(max_length=50, blank=True)
    URL = models.URLField(blank=True)

    def __unicode__(self):
        return self.TiTLE

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"

class MagicForm(ModelForm):
 
    class Meta:
        model = Magic