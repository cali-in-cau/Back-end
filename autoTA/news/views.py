from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.

import requests

def index(request):
    url = "https://google-news.p.rapidapi.com/v1/topic_headlines"

    querystring = {"lang": "en", "country": "US", "topic": "business"}

    headers = {
        'x-rapidapi-key': "5dd3a7daf5msh8aab6de8f4a3c93p1069c3jsnd645a395d8a8",
        'x-rapidapi-host': "google-news.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    

    return render(request, 'index.html')

