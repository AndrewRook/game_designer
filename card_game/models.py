from django.db import models
from user_control.models import UserProfile


# Create your models here.
class Card(models.Model):
    creature = 'CR'
    spell = 'SP'
    card_type_choices = ((creature,'Creature'),(spell,'Spell'))
    type = models.CharField(max_length=2,choices=card_type_choices,default=creature)
    name = models.CharField(max_length=64)
    cost = models.IntegerField(default=0)
    art = models.ImageField(upload_to='card_images',blank=True)
    text = models.TextField(default='')
    power = models.IntegerField(default=0)
    toughness = models.IntegerField(default=1)
    change_author = models.ForeignKey(UserProfile)
    change_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name
    
class Unique_Card(models.Model):
    card_id = models.ForeignKey(Card)

    def __unicode__(self):
        return str(self.pk)
    
class Unique_Version(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=256)
    creation_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class Version(models.Model):
    version_number = models.ForeignKey(Unique_Version)
    card_id = models.ForeignKey(Card)

    def __unicode__(self):
        return str(self.pk)
