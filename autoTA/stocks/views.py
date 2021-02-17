from typing import Dict, Any

from django.shortcuts import render
from django.http import HttpResponse
from autoTA.utils import stocks_api
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
from .models import Stock
from django.contrib import messages
import requests


# Create your views here.
def index(request):
    return render(request, 'index.html')

def save_stocks(request):
    stocks_api.save_stocks_data_in_db()
    print('data is saved')
    return render(request,'index.html')

def delete_stocks(request):
    stocks_api.delete_stocks_data()
    print('data is deleted')
    return render(request, 'index.html')

# front -> back, 단순 그래프 정보만 리턴
def stock_graph(request):
    date_type = request.GET.get('date_type')
    start_date = request.GET.get('start_date')
    stock_code = request.GET.get('stock_code')
    data = stocks_api.get_stock_data(stock_code,date_type,start_date)
    data = json.dumps(data, cls=DjangoJSONEncoder,ensure_ascii = False)
    print('show the stock data')
    return HttpResponse(data)
    #return render(request, 'show_graph.html',{"data":data})

# front -> back 으로 predict 정보를 요청할 때
def stock_predict(request):
    date_type = request.GET.get('date_type')
    start_date = request.GET.get('start_date')
    stock_code = request.GET.get('stock_code')
    print(date_type,start_date,stock_code)
    data = stocks_api.get_stock_data(stock_code,date_type,start_date)
    data = json.dumps(data, cls=DjangoJSONEncoder,ensure_ascii = False)
    res = requests.post('http://localhost:8888/ml/predict', data)
    result = {'predict':json.loads(res.text),'data':json.loads(data)}
    result = json.dumps(result, cls=DjangoJSONEncoder,ensure_ascii = False)
    return HttpResponse(result)

def search_stock(request,keyword):
    stocks = Stock.objects.all()
    # keyword = request.GET.get('keyword', '')  # 검색어
    stock_data = []
    context = {}
    if keyword:
        stock_with_keyword = stocks.filter(stock_name__icontains=keyword)
        for stock in stock_with_keyword:
            name = stock.stock_name
            code = stock.stock_code
            data = {'name': name, 'code': code}
            stock_data.append(data)
    context['result'] = stock_data
    context = json.dumps(context, cls=DjangoJSONEncoder,ensure_ascii = False)
    print(context)
    return HttpResponse(context)

def search_stock_with_code(request, stock_code):
    stock = Stock.objects.get(stock_code = stock_code)
    if stock_code:
        name = stock.stock_name
        code = stock.stock_code
        stockType = stock.stock_type
        industry = stock.stock_industry

        context = {'name': name, 'code': code, 'type': stockType, 'industry': industry}
        context = json.dumps(context, cls=DjangoJSONEncoder,ensure_ascii = False)
        print(context)
    return HttpResponse(context)

