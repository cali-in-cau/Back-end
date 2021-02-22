from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail as sm
from django.conf import settings
from users.models import User
from users.models import Favorite
from stocks.models import Stock
from autoTA.utils import stocks_api
# Create your views here.

def send_mail(request):

    user_data = User.objects.all() # user saved in DataBase
    user_list = []

    user_favorite = Favorite.objects.values('stock','user')
    favorites = {} # {user:stock lists}
    user_favorite_stocks_name = []

    stock_data = Stock.objects.all()

    for user in user_data:
        user_list.append(user.email)
        stock_lists = user_favorite.filter(user = user)
        # for stock in stock_lists:
        #     stock.stock_name
        #     # user_favorite_stocks_name.append(stock.stock_name)
        favorites[user.email] = stock_lists

    for user_email in favorites.keys():

        res = sm(
            subject = '[StockReader] Time to read your stock graph',
            message = f'Time to check your stocks! {favorites[user_email]} : BULL ',
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [user_email],
            fail_silently = False
        )


    return HttpResponse(f"Email sent to members")