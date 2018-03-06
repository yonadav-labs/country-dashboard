# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Address(models.Model):
    name = models.CharField(max_length=255)
    account_id = models.IntegerField()
    address_street_1 = models.CharField(max_length=255)
    address_street_2 = models.CharField(max_length=255)
    address_city = models.CharField(max_length=255)
    address_state = models.CharField(max_length=255)
    address_zip = models.CharField(max_length=255)
    callback_number_id = models.CharField(max_length=255)
    location_id = models.IntegerField(null=True)
    enabled = models.BooleanField(default=True)    
    search_index = models.TextField(max_length=255, null=True, blank=True)    
    latitude = models.FloatField()
    longitude = models.FloatField()
    voiceaxis_id = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'e911_registrations'
