from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.


def index(request):
    newsapi = NewsApiClient(api_key="a898ddc1-35f2-42c3-ac04-dd6f9cbf3a8a")
    topheadlines = newsapi.get_top_headlines(sources='al-jazeera-english')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)



    return render(request, 'index.html', context={"mylist":mylist})
