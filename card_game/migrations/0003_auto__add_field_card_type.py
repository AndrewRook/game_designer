# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Card.type'
        db.add_column(u'card_game_card', 'type',
                      self.gf('django.db.models.fields.CharField')(default='CR', max_length=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Card.type'
        db.delete_column(u'card_game_card', 'type')


    models = {
        u'card_game.card': {
            'Meta': {'object_name': 'Card'},
            'art': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'power': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'toughness': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'CR'", 'max_length': '2'})
        },
        u'card_game.unique_card': {
            'Meta': {'object_name': 'Unique_Card'},
            'card_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['card_game.Card']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'card_game.unique_version': {
            'Meta': {'object_name': 'Unique_Version'},
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'card_game.version': {
            'Meta': {'object_name': 'Version'},
            'card_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['card_game.Card']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'version_number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['card_game.Unique_Version']"})
        }
    }

    complete_apps = ['card_game']