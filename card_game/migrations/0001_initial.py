# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'cards'
        db.create_table(u'card_game_cards', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('art', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('power', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('toughness', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'card_game', ['cards'])

        # Adding model 'unique_cards'
        db.create_table(u'card_game_unique_cards', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('card_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['card_game.cards'])),
        ))
        db.send_create_signal(u'card_game', ['unique_cards'])

        # Adding model 'unique_versions'
        db.create_table(u'card_game_unique_versions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'card_game', ['unique_versions'])

        # Adding model 'versions'
        db.create_table(u'card_game_versions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('version_number', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['card_game.unique_versions'])),
            ('card_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['card_game.cards'])),
        ))
        db.send_create_signal(u'card_game', ['versions'])


    def backwards(self, orm):
        # Deleting model 'cards'
        db.delete_table(u'card_game_cards')

        # Deleting model 'unique_cards'
        db.delete_table(u'card_game_unique_cards')

        # Deleting model 'unique_versions'
        db.delete_table(u'card_game_unique_versions')

        # Deleting model 'versions'
        db.delete_table(u'card_game_versions')


    models = {
        u'card_game.cards': {
            'Meta': {'object_name': 'cards'},
            'art': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'power': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'toughness': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'card_game.unique_cards': {
            'Meta': {'object_name': 'unique_cards'},
            'card_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['card_game.cards']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'card_game.unique_versions': {
            'Meta': {'object_name': 'unique_versions'},
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'card_game.versions': {
            'Meta': {'object_name': 'versions'},
            'card_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['card_game.cards']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'version_number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['card_game.unique_versions']"})
        }
    }

    complete_apps = ['card_game']