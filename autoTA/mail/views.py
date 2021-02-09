from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail as sm
from django.conf import settings
# Create your views here.

# def email(request):
#
#     subject = '[StockReader] Time to check your stock at StockReader'
#     message = 'Time to sell the stock!! go to the link'
#     email_from = settings.EMAIL_HOST_USER
#     recipeint_list = ['mjwoo0@naver.com',] #user
#
#     send_mail(subject, message, email_from, recipeint_list)
#
#     return redirect('redirect to a new page')

def send_mail(request):
    res = sm(
        subject = '[StockReader] Time to check your stock at StockReader',
        message = 'Time to sell the stock!! go to the link',
        from_email = settings.EMAIL_HOST_USER,
        recipient_list = ['mjwoo001@gmail.com'],
        fail_silently = False
    )

    return HttpResponse(f"Email sent to {res} members")