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
    user_id = request.user
    stocks_api.add_favorite(user_id,stock_code)
    favorites = stocks_api.get_favorites(user_id)
    favorites = json.dumps(favorites, cls=DjangoJSONEncoder,ensure_ascii = False)
    return HttpResponse(favorites)

def delete_favorite(request, stock_code):
    user_id = request.user
    stocks_api.delete_favorite(user_id,stock_code)
    favorites = stocks_api.get_favorites(user_id)
    favorites = json.dumps(favorites, cls=DjangoJSONEncoder,ensure_ascii = False)
    return HttpResponse(favorites)

def get_favorites(request):
    user_id = request.user
    favorites = stocks_api.get_favorites(user_id)
    favorites = json.dumps(favorites, cls=DjangoJSONEncoder,ensure_ascii = False)
    return HttpResponse(favorites)