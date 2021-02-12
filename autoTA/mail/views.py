from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail as sm
from django.conf import settings
from users.models import User
# Create your views here.

def send_mail(request):

    user_data = User.objects.all() # user saved in DataBase
    user_list = []

    for user in user_data:
        user_list.append(user.email)

    res = sm(
        subject = '[StockReader] Time to check your stock at StockReader',
        message = 'Time to sell the stock!! Visit StockReader website and get more details.',
        from_email = settings.EMAIL_HOST_USER,
       # recipient_list = user_list,
        recipient_list = [
            'mjwoo0@naver.com'
        ],
        fail_silently = False
    )

    return HttpResponse(f"Email sent to {res} members")

def mail(request, state):

