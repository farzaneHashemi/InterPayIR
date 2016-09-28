from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class   UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="UserProfile")
    name = models.CharField(max_length=30, null=False, blank=False)
    picture = models.ImageField(upload_to='userProfiles/', null=False, blank=False)
    email = models.EmailField

    def __str__(self):
        return '{}'.format(self.user.username)

    def __unicode__(self):
        return self.user.username


class CommonUser(models.Model):
    # since we might need to define a Manager model in the future, this model is named as "CommonUser"
    user_ID = models.ForeignKey(UserProfile, null=False, related_name='user_ID')

    def __str__(self):
        return '{} - {}'.format(self.customer_ID, self.user_ID.name)
