from django.contrib.auth.models import User
from django.db import models
from django.forms import ChoiceField
from django_countries.fields import CountryField
from datetime import datetime



# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="UserProfile")
    # name = models.CharField(max_length=30, null=False, blank=False)
    picture = models.ImageField(upload_to='userProfiles/', null=True, blank=True)
    date_of_birth = models.DateTimeField(null=False, blank=False, default=datetime.today())
    country = CountryField(default="Iran")
    national_code = models.IntegerField(null=False, blank=False)
    email = models.EmailField()

    def __str__(self):
        return '{}'.format(self.user.username)

    def __unicode__(self):
        return self.user.username

        # def __init__(self, *args, **kwargs):
        #     super(UserProfile, self).__init__(*args, **kwargs)
        #     if self.instance:
        #         # we're operating on an existing object, not a new one...
        #         country = self.instance.country
        #         cities = self.fields["new_city"] = ChoiceField(choices=cities)


class CommonUser(models.Model):
    # since we might need to define a Manager model in the future, this model is named as "CommonUser"
    user_ID = models.ForeignKey(UserProfile, null=False, related_name='user_ID')

    def __str__(self):
        return '{} - {}'.format(self.customer_ID, self.user_ID.name)
