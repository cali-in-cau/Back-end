import FinanceDataReader as fdr
import pandas as pd
from datetime import datetime
from stocks.models import Stock
from users.models import Favorite,User
from datetime import timedelta
from dateutil.relativedelta import relativedelta


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

def get_stock_data(code, date_type, start_date):
    data = {"info":{},"data":{}}
    stock = Stock.objects.filter(stock_code=code)
    if stock.exists():
        if not date_type in {'month','week','day'}:
            return {'success':'failed', 'message':"wrong date_type"}
        start=datetime.today() - relativedelta(months=int(start_date))
        end=datetime.today().strftime("%Y-%m-%d")
        data["info"]["date_type"] = date_type
        data["info"]["code"] = stock.first().stock_code
        data["info"]["name"] = stock.first().stock_name
        data["info"]["type"] = stock.first().stock_type
        df_graph_data = fdr.DataReader(code,start,end)
        date = []
        value = []
        index_controller = ""
        row_controller = pd.DataFrame(columns=['Close','Open','High','Low','Volume','Change'])
        divider = 0
        for i,row in df_graph_data.iterrows():
            if date_type == 'month':
                if i.strftime('%Y-%m-%d')[0:7] == index_controller:
                    index_controller = i.strftime('%Y-%m-%d')[0:7]
                    row_controller += row
                else:
                    if divider != 0 :
                        date.append(index_controller)
                        value.append((row_controller/divider).to_dict())
                    index_controller = i.strftime('%Y-%m-%d')[0:7]
                    row_controller = row
                    divider = 0
            elif date_type == 'week':
                if i.weekday() == 0:
                    if divider != 0:
                        date.append(index_controller)
                        value.append((row_controller/divider).to_dict())
                    index_controller = i.strftime('%Y-%m-%d')
                    row_controller = row
                    divider = 0
                else:
                    row_controller += row
            elif date_type =='day':
                date.append(i.strftime('%Y-%m-%d'))
                value.append(row.to_dict())
            divider += 1
        data['data']['date'] = date[1:]
        data['data']['value'] = value[1:]
    else:
        return {'success':'failed', 'message':"wrong stock_code"}
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
    user = User.objects.get(email = user_email)
    favorites = Favorite.objects.filter(user=user)
    data = []
    for favorite in favorites:
        data.append({'stock_name':favorite.stock.stock_name,'stock_code':favorite.stock.stock_code})
    return data