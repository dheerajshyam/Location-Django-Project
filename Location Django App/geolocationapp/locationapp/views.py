import requests

from django.shortcuts import render
import json

# Create your views here.

def index(request):
    ip_res = requests.get('https://api.ipify.org').content.decode('utf8')
    location_res = requests.get(f'http://ip-api.com/json/{ip_res}')
    location_json = json.loads(location_res.text)
    return render(request, 'index.html', {'data':location_json})