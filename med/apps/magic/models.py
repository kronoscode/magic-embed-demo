# -*- coding: utf-8 -*-
from django.db import models

class Video(models.Model):

    title = models.CharField("TITLE", max_length=50)
    url = models.URLField("URL", help_text="Video can be from any origin like youtube, vimeo, metacafe, etc")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"

