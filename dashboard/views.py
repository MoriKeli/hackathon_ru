from django.shortcuts import render, redirect
import requests
import json

def index_view(request):
    API_KEY = "yE2wzM3G6eSS5FyhXLzPLsWPihwMFc"
    url_route  = "http://api.kmhfltest.health.go.ke/api/facilities/facilities/?fields=id%2Ccode%2Cname%2Cofficial_name%2Cregulatory_status_name%2Cupdated%2Cfacility_type_name%2Cowner_name%2Ccounty%2Csub_county_name%2Crejected%2Cward_name%2Ckeph_level%2Ckeph_level_name%2Cconstituency_name%2Cis_complete%2Cin_complete_details%2Capproved%2Cis_approved%2Capproved_national_level&format=json"
    

    # REQUEST_URL = f'{BASE_URL}'
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response =  requests.get(url_route, headers=headers)
    data = response.json()
    print(data)

    context = {'response': data}
    return render(request, 'dashboard/index.html', context)

