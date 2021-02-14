from django.shortcuts import render

import requests
import json

def index(request):
    url = "https://google-news.p.rapidapi.com/v1/topic_headlines"
    querystring = {"lang": "en", "country": "US", "topic": "business"}
    headers = {
        'x-rapidapi-key': "5dd3a7daf5msh8aab6de8f4a3c93p1069c3jsnd645a395d8a8",
        'x-rapidapi-host': "google-news.p.rapidapi.com"
    }
    context = {}
    response = requests.request("GET", url, headers=headers, params=querystring)
    news_data = json.loads(response.text) # return data as json format
    print(news_data["articles"])


    print(type(news_data)) #<class 'requests.models.Response'>
    #context['news'] = response.text
    #print(context)
    return render(request, 'index.html',context)

