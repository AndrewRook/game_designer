from django import forms
from card_game.models import Card,Unique_Card,Version,Unique_Version

class CardForm(forms.ModelForm):
    name = forms.CharField(help_text="Card Name:")
    type = forms.CharField(widget=forms.Select(choices=Card.card_type_choices), help_text="Card Type:")
    cost = forms.IntegerField(help_text="Cost:")
    art = forms.ImageField(help_text="Upload Card Art (optional):", required=False)
    text = forms.CharField(widget=forms.Textarea(), help_text="Card Text:", required=False)
    power = forms.IntegerField(help_text="Power:",required=False)
    toughness = forms.IntegerField(help_text="Toughness:",required=False)
    class Meta:
        model = Card
        fields = ['name','type','cost','art','text','power','toughness']
    
    # creature = 'CR'
    # spell = 'SP'
    # card_type_choices = ((creature,'Creature'),(spell,'Spell'))
    # type = models.CharField(max_length=2,choices=card_type_choices,default=creature)
    # name = models.CharField(max_length=64)
    # cost = models.IntegerField(default=0)
    # art = models.ImageField(upload_to='card_images',blank=True)
    # text = models.TextField()
    # power = models.IntegerField(default=0)
    # toughness = models.IntegerField(default=1)
    # change_author = models.ForeignKey(UserProfile)
    # change_date = models.DateField(auto_now_add=True)

