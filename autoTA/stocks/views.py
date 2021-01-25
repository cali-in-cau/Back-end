from django.shortcuts import render
from .utils import stocks_api

# Create your views here.
def index(request):
    return render(request, 'index.html')

def save_stock_data(request):
    stocks_api.save_stock_data_in_db()
    print('data is saved')
    return render(request,'index.html')

def delete_stock_data(request):
    stocks_api.delete_stock_data()
    print('data is deleted')
    return render(request, 'index.html')