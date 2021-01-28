from django.shortcuts import render
from django.http import HttpResponse
from .utils import stocks_api
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def save_stocks_data(request):
    stocks_api.save_stocks_data_in_db()
    print('data is saved')
    return render(request,'index.html')

def delete_stocks_data(request):
    stocks_api.delete_stocks_data()
    print('data is deleted')
    return render(request, 'index.html')

def show_stock_graph(request,stock_code):
    data = stocks_api.get_stock_data(stock_code)
    data = json.dumps(data, cls=DjangoJSONEncoder)
    print('show the stock data')
    return HttpResponse(data)
    #return render(request, 'show_graph.html',{"data":data})

def search_stock_data(request):
    keyword = request.GET.get('keyword','') #검색어
    if keyword:
        stocks_api.get_stock_data(keyword)

    print('searched data name : ')
    return(request, 'index.html')