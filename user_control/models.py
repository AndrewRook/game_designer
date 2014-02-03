from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    display_name = models.CharField(max_length=128)
    can_direct_edit = models.BooleanField(default=False)
    def __unicode(self):
        return self.user.username
