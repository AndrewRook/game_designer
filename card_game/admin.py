from django.contrib import admin
from card_game.models import Card, Unique_Card, Unique_Version, Version

# Register your models here.
admin.site.register(Card)
admin.site.register(Unique_Card)
admin.site.register(Unique_Version)
admin.site.register(Version)
