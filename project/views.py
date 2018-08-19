# Create your views here.
from django.shortcuts import render
import requests

def get_talks(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    return render(request, 'project/talk.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })