from django.shortcuts import render
from newsapi import NewsApiClient
from pandas.io.json import json_normalize

def index(request):

    newsapi = NewsApiClient(api_key = 'c840bf8b562c42388c72529e4459e18e')

    top_headlines = newsapi.get_top_headlines(category='business', language='en', country='us')
    articles = top_headlines['articles']
    context = {'news': articles}
    print(context)

    return render(request, 'index.html', context)

