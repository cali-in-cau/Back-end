from django.shortcuts import render
from django.http import HttpResponse
from autoTA.utils import stocks_api
from .models import User,Favorite
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
def LoginView(request):
    return render(request, "login.html")

def SuccessView(request):
    return render(request, "success.html")


def add_favorite(request, stock_code):
    data = json.loads(request.body)
    user_id = data['email']
    stocks_api.add_favorite(user_id,stock_code)
    favorites = stocks_api.get_favorites(user_id)
    favorites = json.dumps(favorites, cls=DjangoJSONEncoder,ensure_ascii = False)
    return HttpResponse(favorites)

def delete_favorite(request, stock_code):
    data = json.loads(request.body)
    user_id = data['email']
    stocks_api.delete_favorite(user_id,stock_code)
    favorites = stocks_api.get_favorites(user_id)
    favorites = json.dumps(favorites, cls=DjangoJSONEncoder,ensure_ascii = False)
    return HttpResponse(favorites)

def get_favorites(request):
    data = json.loads(request.body)
    user_id = data['email']
    favorites = stocks_api.get_favorites(user_id)
    favorites = json.dumps(favorites, cls=DjangoJSONEncoder,ensure_ascii = False)
    return HttpResponse(favorites)

def get_user(request):
    data = json.loads(request.body)
    print(data)
    valid = stocks_api.valid_user(data['email'])
    if(valid):
        user = stocks_api.get_user_info(data['email'])
        success = True
        response = HttpResponse(success)
        response.set_cookie('token',user)
        return response
    else:
        success = False
        return HttpResponse(success)