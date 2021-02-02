import FinanceDataReader as fdr
import pandas as pd
from datetime import datetime
from stocks.models import Stock
from users.models import Favorite,User


def save_in_db(stock_df,index='none'):
    for row in stock_df.itertuples():
        name = row.Name
        code = row.Symbol
        industury = row.Industry
        if not Stock.objects.filter(stock_code=code).exists():
            stock = Stock(stock_code=code,stock_name=name,stock_type=index,stock_industry=industury)
            stock.save()

def save_stocks_data_in_db():
    kospi_df = fdr.StockListing('KOSPI')
    kosdaq_df = fdr.StockListing('KOSDAQ')
    nasdaq_df = fdr.StockListing('NASDAQ')
    save_in_db(kospi_df,'KOSPI')
    save_in_db(kosdaq_df,'KOSDAQ')
    save_in_db(nasdaq_df,'NASDAQ')

def delete_stocks_data():
    Stock.objects.all().delete()

def get_stock_data(code):
    data = {"info":{},"data":{}}
    stock = Stock.objects.filter(stock_code=code)
    if stock.exists():
        start=datetime(2020,1,4)
        end=datetime.today().strftime("%Y-%m-%d")
        data["info"]["code"] = stock.first().stock_code
        data["info"]["name"] = stock.first().stock_name
        data["info"]["type"] = stock.first().stock_type
        data["info"]["industry"] = stock.first().stock_industry
        df_graph_data = fdr.DataReader(code,start,end)
        date = []
        value = []
        for i,row in df_graph_data.iterrows():
            date.append(i.strftime('%Y-%m-%d'))
            value.append(row.to_dict())
        data['data']['date'] = date
        data['data']['value'] = value
        #print(data)
    return data

def add_favorite(user_email,favorite_code):
    user = User.objects.get(email=user_email)
    stock = Stock.objects.get(stock_code=favorite_code)
    favorite = Favorite.objects.filter(user=user, stock= stock)
    if not favorite.exists():
        favorite = Favorite(user=user, stock= stock)
        favorite.save()

def delete_favorite(user_email,favorite_code):
    user = User.objects.get(email=user_email)
    stock = Stock.objects.get(stock_code=favorite_code)
    favorite = Favorite.objects.filter(user=user, stock= stock)
    if favorite.exists():
        favorite.delete()

def get_favorites(user_email):
    favorites = Favorite.objects.filter(user=user_email)
    data = []
    for favorite in favorites:
        data.append({'stock_name':favorite.stock.stock_name,'stock_code':favorite.stock.stock_code})
    return data