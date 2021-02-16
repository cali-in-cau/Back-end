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
    #data = json.dumps(data, cls=DjangoJSONEncoder,ensure_ascii = False)
    #res = requests.post('http://yaeoni.o-r.kr/ml/predict', data)
    #res = json.dumps(res, cls=DjangoJSONEncoder,ensure_ascii = False)
    predict1 = {'bull': [('LONGLEGGEDDOJI_BULL', '2021-01-01'), ('RICKSHAWMAN_BULL', '2021-01'), ('DOJI_BULL', '2021-01')], 'bear': [('SPINNINGTOP_BEAR', '2021-01'), ('HIGHWAVE_BEAR', '2021-01')]}
    predict2 = [('CDLHIGHWAVE_BULL', 0.23239417374134064), ('CDLSPINNINGTOP_BULL', 0.17750932276248932), ('CDLDOJI_BULL', 0.16139625012874603), ('CDLLONGLEGGEDDOJI_BULL', 0.16064831614494324), ('CDLRICKSHAWMAN_BULL', 0.1514437049627304), ('CDLSHOOTINGSTAR_BEAR', 0.07264261692762375), ('CDLSHORTLINE_BULL', 0.022190740332007408), ('CDLHIKKAKE_BULL', 0.0036282148212194443), ('CDLCLOSINGMARUBOZU_BULL', 0.0033749474678188562), ('CDLLONGLINE_BULL', 0.0017008588183671236), ('CDLHIGHWAVE_BEAR', 0.0016671207267791033), ('CDLBELTHOLD_BULL', 0.0014224122278392315), ('CDLMARUBOZU_BULL', 0.0013502076035365462), ('CDLHARAMI_BULL', 0.0010560705559328198), ('CDLCLOSINGMARUBOZU_BEAR', 0.0010419032769277692), ('CDLSPINNINGTOP_BEAR', 0.000916561926715076), ('CDLSHORTLINE_BEAR', 0.0008280221954919398), ('CDLHARAMI_BEAR', 0.0008256369037553668), ('CDLHAMMER_BULL', 0.0007462479989044368), ('CDLENGULFING_BULL', 0.0005013130721636117), ('CDLLONGLINE_BEAR', 0.00044498054194264114), ('CDLHANGINGMAN_BEAR', 0.00043029882363043725), ('CDLENGULFING_BEAR', 0.00041407151729799807), ('CDLMARUBOZU_BEAR', 0.00039904977893456817), ('CDLBELTHOLD_BEAR', 0.00029871377046220005), ('CDLHIKKAKE_BEAR', 0.00024970516096800566), ('CDL3OUTSIDE_BEAR', 0.0001835259608924389), ('CDLMATCHINGLOW_BULL', 0.00016953315935097635), ('CDL3OUTSIDE_BULL', 0.00012544318451546133)]
    result = {'predict1':predict1,'predict2':predict2,'data':data}
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

