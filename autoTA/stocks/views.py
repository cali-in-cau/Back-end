from django.shortcuts import render
from .utils import stocks_api

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

def show_stock_graph(request):
    data = stocks_api.get_stock_data('238490.KQ')
    print('show the stock data')
    return render(request, 'show_graph.html',{"data":data})