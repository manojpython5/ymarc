# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User)


class vegetables(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(null=True)


class NonVeg(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(null=True)

class Dairy(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(null=True)
