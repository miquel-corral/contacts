# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'contactsapp_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal(u'contactsapp', ['Tag'])

        # Adding model 'Contact'
        db.create_table(u'contactsapp_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('email1', self.gf('django.db.models.fields.EmailField')(max_length=250, null=True, blank=True)),
            ('email2', self.gf('django.db.models.fields.EmailField')(max_length=250, null=True, blank=True)),
            ('telephone1', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('mobile1', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('mobile2', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'contactsapp', ['Contact'])

        # Adding M2M table for field tags on 'Contact'
        m2m_table_name = db.shorten_name(u'contactsapp_contact_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contact', models.ForeignKey(orm[u'contactsapp.contact'], null=False)),
            ('tag', models.ForeignKey(orm[u'contactsapp.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contact_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'contactsapp_tag')

        # Deleting model 'Contact'
        db.delete_table(u'contactsapp_contact')

        # Removing M2M table for field tags on 'Contact'
        db.delete_table(db.shorten_name(u'contactsapp_contact_tags'))


    models = {
        u'contactsapp.contact': {
            'Meta': {'object_name': 'Contact'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'email1': ('django.db.models.fields.EmailField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'email2': ('django.db.models.fields.EmailField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'mobile1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'mobile2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['contactsapp.Tag']", 'symmetrical': 'False'}),
            'telephone1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'contactsapp.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['contactsapp']