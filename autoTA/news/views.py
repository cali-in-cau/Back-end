from django.shortcuts import render
from newsapi.newsapi_client import NewsApiClient
from django.http import HttpResponse, JsonResponse
import datetime as dt
import pandas as pd
import requests
from pandas.io.json import json_normalize


def index(request):
    newsapi = NewsApiClient(api_key = 'c840bf8b562c42388c72529e4459e18e')
    top_headlines = newsapi.get_top_headlines(category='business', language='en', country='us')
    articles = top_headlines['articles']

    context = {}
    news_data = []
    for article in top_headlines['articles']:
        title = article['title']
        description = article['description']
        img = article['urlToImage']
        url = article['url']
        news = {'title':title, 'desc': description, 'img': img, 'url': url}
        news_data.append(news)
    context = {'news': news_data}
    print(context)
    return JsonResponse(context)

