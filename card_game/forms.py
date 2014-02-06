from django import forms
from card_game.models import Card,Unique_Card,Version,Unique_Version

class CardForm(forms.ModelForm):
    name = forms.CharField(help_text="Card Name:")
    type = forms.CharField(widget=forms.Select(choices=Card.card_type_choices), help_text="Card Type:")
    class Meta:
        model = Card
        fields = ['name','type']
    
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

# class UserForm(forms.ModelForm):
#     username = forms.CharField(help_text="Please enter a username.")
#     email = forms.CharField(help_text="Please enter your email.")
#     password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

# class UserProfileForm(forms.ModelForm):
#     display_name = forms.CharField(help_text="What should we call you?")
#     class Meta:
#         model = UserProfile
#         fields = ['display_name']#Hiding the can_direct_edit 
