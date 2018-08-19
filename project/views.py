# Create your views here.
from django.shortcuts import render
import requests

def project_update_talk(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    print geodata
    return render(request, 'project/talk.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })