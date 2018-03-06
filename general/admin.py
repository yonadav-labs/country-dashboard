# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from general.models import *

class AddressAdmin(admin.ModelAdmin):
    list_display = ['name', 'address_city', 'address_state', 'address_street_1', 'address_street_2', 
                    'address_zip', 'latitude', 'longitude']
    search_fields = ['name', 'address_street_1', 'address_street_2', 'address_city', 'address_state', 
                    'address_zip', 'latitude', 'longitude']

admin.site.register(Address, AddressAdmin)
