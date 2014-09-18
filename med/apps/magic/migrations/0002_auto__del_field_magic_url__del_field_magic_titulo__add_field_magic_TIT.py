# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'magic.url'
        db.delete_column(u'magic_magic', 'url')

        # Deleting field 'magic.titulo'
        db.delete_column(u'magic_magic', 'titulo')

        # Adding field 'Magic.TITLE'
        db.add_column(u'magic_magic', 'TITLE',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'Magic.URL'
        db.add_column(u'magic_magic', 'URL',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'magic.url'
        db.add_column(u'magic_magic', 'url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'magic.titulo'
        db.add_column(u'magic_magic', 'titulo',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Deleting field 'Magic.TITLE'
        db.delete_column(u'magic_magic', 'TITLE')

        # Deleting field 'Magic.URL'
        db.delete_column(u'magic_magic', 'URL')


    models = {
        u'magic.magic': {
            'Meta': {'object_name': 'Magic'},
            'TITLE': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['magic']