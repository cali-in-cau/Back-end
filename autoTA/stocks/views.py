from django.shortcuts import render
import requests
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def stock(request):
    api_request = requests.get('url')
