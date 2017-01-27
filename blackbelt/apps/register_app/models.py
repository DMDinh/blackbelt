from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

class Quote(models.Model):
    author = models.CharField(max_length = 100)
    quote = models.CharField(max_length =100)
    user = models.ForeignKey("User", default=1)

class Favorite(models.Model):
    quote = models.ForeignKey("Quote", null=True)
    user = models.ForeignKey("User", null=True)
