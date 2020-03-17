from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    UNITEDKINGDOM = 'UK'
    UNITEDSTATES = 'US'
    IRELAND = 'IR'
    SCOTLAND = 'SC'
    WALES = 'WA'

    COUNTRY_CHOICES = (
        (UNITEDKINGDOM, 'United Kingdom'),
        (UNITEDSTATES, 'United States of America'),
        (IRELAND, 'Ireland'),
        (SCOTLAND, 'Scotland'),
        (WALES, 'Wales'),
    )



    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=13)
    address1 = models.CharField(max_length=75)
    town = models.CharField(max_length=20)
    county = models.CharField(max_length=20)
    postcode = models.CharField(max_length=8)
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES, default=UNITEDKINGDOM)

    def __str__(self):
        return self.user.username