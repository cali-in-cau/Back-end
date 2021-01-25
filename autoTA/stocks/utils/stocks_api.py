import pandas_datareader as pdr
import pandas as pd
from datetime import datetime
from ..models import Stock

# 종목 타입에 따라 download url이 다름.종목코드 뒤에.KS.KQ등이 입력되어야해서 Download Link 구분 필요
stock_type = {
    'kospi': 'stockMkt',
    'kosdaq': 'kosdaqMkt'
}
# 회사명으로 주식 종목 코드를 획득할 수 있도록 하는 함수
def get_code(df, name): 
    code = df.query("name=='{}'".format(name))['code'].to_string(index = False)
# 위와같이 code명을 가져오면 앞에 공백이 붙어있는 상황이 발생하여 앞뒤로 sript()하여 공백 제거
    code = code.strip()
    return code
# download url 조합
def get_download_stock(market_type = None): 
    market_type = stock_type[market_type]
    download_link = 'http://kind.krx.co.kr/corpgeneral/corpList.do'
    download_link = download_link + '?method=download'
    download_link = download_link + '&marketType=' + market_type
    df = pd.read_html(download_link, header = 0)[0]
    return df;
# kospi 종목코드 목록 다운로드
def get_download_kospi(): 
    df = get_download_stock('kospi')
    df.종목코드 = df.종목코드.map('{:06d}.KS'.format)
    return df
# kosdaq 종목코드 목록 다운로드
def get_download_kosdaq(): 
    df = get_download_stock('kosdaq')
    df.종목코드 = df.종목코드.map('{:06d}.KQ'.format)
    return df


def save_stocks_data_in_db():
    # kospi,kosdaq 종목코드 각각 다운로드
    kospi_df = get_download_kospi()
    kosdaq_df = get_download_kosdaq()

    # data frame정리
    kospi_df = kospi_df[
        ['회사명', '종목코드']
    ]
    kosdaq_df = kosdaq_df[
        ['회사명', '종목코드']
    ]
    # data frame title 변경 '회사명' = name, 종목코드 = 'code'
    kospi_df = kospi_df.rename(columns = {
        '회사명': 'name',
        '종목코드': 'code'
    })
    kosdaq_df = kosdaq_df.rename(columns = {
        '회사명': 'name',
        '종목코드': 'code'
    })
    code_df = pd.concat([kospi_df, kosdaq_df])
    for row in code_df.itertuples():
        name = row.name
        code = row.code
        print(name,code)
        if not Stock.objects.filter(stock_code=code).exists():
            print(name,code)
            stock = Stock(stock_code=code,stock_name=name)
            stock.save()

def delete_stocks_data():
    Stock.objects.all().delete()

def get_stock_data(code):
    data = {'info':{},'data':{}}
    stock = Stock.objects.filter(stock_code=code)
    if stock.exists():
        start_date = '1996-05-06'
        data['info']['code'] = stock.first().stock_code
        data['info']['name'] = stock.first().stock_name
        df_graph_data = pdr.get_data_yahoo(code,start_date)['Close']
        #raw_data = df_graph_data.to_json(orient='table')
        date = []
        close = []
        for index,value in enumerate(df_graph_data):
            date.append(value)
            close.append(df_graph_data.index[index])
        data['data']['date'] = date
        data['data']['close'] = close
    print(data)
    return data
    #code = get_code(code_df, '삼성전자')
    # get_data_yahoo API를 통해서 yahho finance의 주식 종목 데이터를 가져온다.df = pdr.get_data_yahoo(code)
