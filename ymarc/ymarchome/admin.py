# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ymarchome.models import vegetables,NonVeg,Dairy,UserProfileInfo

# Register your models here.

admin.site.register(vegetables)
admin.site.register(NonVeg)
admin.site.register(Dairy)
admin.site.register(UserProfileInfo)
