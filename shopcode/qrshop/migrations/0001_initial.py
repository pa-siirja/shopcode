# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Book'
        db.create_table(u'qrshop_book', (
            (u'product_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['shop.Product'], unique=True, primary_key=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cover_picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'qrshop', ['Book'])


    def backwards(self, orm):
        # Deleting model 'Book'
        db.delete_table(u'qrshop_book')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'qrshop.book': {
            'Meta': {'ordering': "['author']", 'object_name': 'Book', '_ormbases': ['shop.Product']},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cover_picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'product_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['shop.Product']", 'unique': 'True', 'primary_key': 'True'})
        },
        'shop.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_shop.product_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'})
        }
    }

    complete_apps = ['qrshop']