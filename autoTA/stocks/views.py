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
    return HttpResponse('data is saved')

def delete_stocks(request):
    stocks_api.delete_stocks_data()
    return HttpResponse('data is deleted')

# front -> back, 단순 그래프 정보만 리턴
def stock_graph(request):
    date_type = request.GET.get('date_type')
    start_date = request.GET.get('start_date')
    stock_code = request.GET.get('stock_code')
    data = stocks_api.get_stock_data(stock_code,date_type,start_date)
    data = json.dumps(data, cls=DjangoJSONEncoder,ensure_ascii = False)
    return HttpResponse(data)
    #return render(request, 'show_graph.html',{"data":data})

# front -> back 으로 predict 정보를 요청할 때
def stock_predict_pattern(request):
    date_type = request.GET.get('date_type')
    stock_code = request.GET.get('stock_code')
    data = None
    if(date_type=='day'):
        data = stocks_api.get_stock_data(stock_code,date_type,21)
    if(date_type=='week'):
        data = stocks_api.get_stock_data(stock_code,date_type,100)
    if(date_type=='month'):
        data = stocks_api.get_stock_data(stock_code,date_type,365)
    data = json.dumps(data, cls=DjangoJSONEncoder,ensure_ascii = False)
    res = requests.post('http://yaeoni.o-r.kr/ml/predict', data)
    result = json.loads(res.text)
    image_prediction = result['image_prediction']
    talib = result['talib']
    talibv2 = result['talibv2']
    result = {'image_prediction':image_prediction,'talib':talib,'talibv2':talibv2}
    result = json.dumps(result, cls=DjangoJSONEncoder,ensure_ascii = False)
    return HttpResponse(result)

# front -> back 으로 predict 정보를 요청할 때
def stock_predict_stockinfo(request):
    date_type = request.GET.get('date_type')
    stock_code = request.GET.get('stock_code')
    data = None
    if(date_type=='day'):
        data = stocks_api.get_stock_data(stock_code,date_type,15)
    if(date_type=='week'):
        data = stocks_api.get_stock_data(stock_code,date_type,100)
    if(date_type=='month'):
        data = stocks_api.get_stock_data(stock_code,date_type,365)
    data = json.dumps(data, cls=DjangoJSONEncoder,ensure_ascii = False)
    res = requests.post('http://yaeoni.o-r.kr/ml/predict', data)
    result = json.loads(res.text)['price_prediction']
    result = json.dumps(result, cls=DjangoJSONEncoder,ensure_ascii = False)
    return HttpResponse(result)

def search_stock(request):
    keyword = request.GET.get('keyword')
    stocks = Stock.objects.all()
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

def search_stock_with_code(request):
    code = request.GET.get('stock_code')
    stock = Stock.objects.get(stock_code = code)
    if code:
        name = stock.stock_name
        stockType = stock.stock_type
        industry = stock.stock_industry
        context = {'name': name, 'code': code, 'type': stockType, 'industry': industry}
        context = json.dumps(context, cls=DjangoJSONEncoder,ensure_ascii = False)
        print(context)
    return HttpResponse(context)

