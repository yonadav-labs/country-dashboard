# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import render
from django.db.models import Count
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from .models import *

def index(request):
    state_freq = {}
    for ii in Address.objects.values('address_state').annotate(count=Count('address_state')): 
        state_freq[ii['address_state']] = ii['count']
    
    return render(request, 'index.html', {'state_freq': json.dumps(state_freq)})

@csrf_exempt
def city_freq(request):
    state = request.POST.get('state')
    county_freq = {}

    for ii in Address.objects.filter(address_state=state).values('address_city').annotate(count=Count('address_city')): 
        county = ''
        for row in settings.CMC:
            if state == row['State short'] and ii['address_city'].lower().strip() == row['City'].lower().strip():
                county = row['County']
                if county in county_freq:
                    county_freq[county] = county_freq[county] + ii['count']
                else:
                    county_freq[county] = ii['count']
                break
        if not county:
            print ii['address_city'].lower().strip(), state, ii['count']

    return JsonResponse(county_freq, safe=False)
