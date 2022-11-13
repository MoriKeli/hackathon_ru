from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
import requests
import json

def index_view(request):
    API_KEY = "yE2wzM3G6eSS5FyhXLzPLsWPihwMFc"
    BASE_URL = "http://api.kmhfltest.health.go.ke/api/facilities/facilities/?fields=id%2Ccode%2Cname%2Cofficial_name%2Cregulatory_status_name%2Cupdated%2Cfacility_type_name%2Cowner_name%2Ccounty%2Csub_county_name%2Crejected%2Cward_name%2Ckeph_level%2Ckeph_level_name%2Cconstituency_name%2Cis_complete%2Cin_complete_details%2Capproved%2Cis_approved%2Capproved_national_level&format=json"
    

    headers = {'Authorization': f'Bearer {API_KEY}'}
    response =  requests.get(BASE_URL, headers=headers)
    
    filter_data = {}
    if response.status_code == 200:
        data = response.json()
        
        filter_data = {
            'county': data["results"][0]["county"],
            'sub_county': data["results"][0]["sub_county_name"],
            'constituency_name': data["results"][0]["constituency_name"],
            'ward': data["results"][0]["ward_name"],

        }
    
    else:
        return HttpResponseForbidden('Authentication verification failed!', response.status_code)

    context = {
        'total_count': data,
        'county': filter_data['county'],
        'sub_county': filter_data["sub_county"],
        'constituency': filter_data["constituency_name"],
        'ward': filter_data["ward"]
    }
    return render(request, 'dashboard/index.html', context)