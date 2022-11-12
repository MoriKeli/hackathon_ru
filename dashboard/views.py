from django.shortcuts import render, redirect
import requests
import json

def index_view(request):
    API_KEY = "7tjuWYGmbmh3VRFytATeoSQqeaZ1CS"
    BASE_URL = "http://api.kmhfltest.health.go.ke/api/facilities/facilities/?format=json"

    REQUEST_URL = f''
    response =  requests.get(REQUEST_URL)
    
    print(response.json())

    context = {}
    return render(request, 'templates/index.html', context)

