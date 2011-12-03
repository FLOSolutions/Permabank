# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'RecordResponse'
        db.create_table('records_recordresponse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Record'])),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sent_responses', to=orm['profiles.Profile'])),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(related_name='received_responses', to=orm['profiles.Profile'])),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.RecordResponse'], null=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('records', ['RecordResponse'])


    def backwards(self, orm):
        
        # Deleting model 'RecordResponse'
        db.delete_table('records_recordresponse')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'profiles.profile': {
            'Meta': {'object_name': 'Profile'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'records.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'records.gift': {
            'Meta': {'object_name': 'Gift', '_ormbases': ['records.Record']},
            'record': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['records.Record']", 'unique': 'True', 'primary_key': 'True'})
        },
        'records.record': {
            'Meta': {'object_name': 'Record'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Category']"}),
            'contact_info': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'other_user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'records_fulfilled'", 'null': 'True', 'to': "orm['profiles.Profile']"}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'default': "'/static/placeholder.jpg'", 'max_length': '100', 'blank': 'True'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'records_created'", 'to': "orm['profiles.Profile']"})
        },
        'records.recordresponse': {
            'Meta': {'object_name': 'RecordResponse'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.RecordResponse']", 'null': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'received_responses'", 'to': "orm['profiles.Profile']"}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Record']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sent_responses'", 'to': "orm['profiles.Profile']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'records.wish': {
            'Meta': {'object_name': 'Wish', '_ormbases': ['records.Record']},
            'record': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['records.Record']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['records']
