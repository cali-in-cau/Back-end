from django.shortcuts import render
from django.http import HttpResponse
from autoTA.utils import stocks_api
from users.authentication import auth
from .models import User,Favorite
import json
from django.core.serializers.json import DjangoJSONEncoder

def add_favorite(request, stock_code):
    data = request.COOKIES
    if 'token' in data:
        user_email = data['token']
        if auth.valid_user(user_email):
            stocks_api.add_favorite(user_email,stock_code)
            favorites = stocks_api.get_favorites(user_email)
            favorites = json.dumps(favorites, cls=DjangoJSONEncoder,ensure_ascii = False)
            return HttpResponse(favorites)
    success = {'success':False, 'message':"no user"}
    return HttpResponse(json.dumps(success))

def delete_favorite(request, stock_code):
    data = request.COOKIES
    if 'token' in data:
        user_email = data['token']
        if auth.valid_user(user_email):
            stocks_api.delete_favorite(user_email,stock_code)
            favorites = stocks_api.get_favorites(user_email)
            favorites = json.dumps(favorites, cls=DjangoJSONEncoder,ensure_ascii = False)
            return HttpResponse(favorites)
    success = {'success':False, 'message':"no user"}
    return HttpResponse(json.dumps(success))

def get_favorites(request):
    data = request.COOKIES
    if 'token' in data:
        user_email = data['token']
        if auth.valid_user(user_email):
            favorites = stocks_api.get_favorites(user_email)
            favorites = json.dumps(favorites, cls=DjangoJSONEncoder,ensure_ascii = False)
            return HttpResponse(favorites)
    success = {'success':False, 'message':"no user"}
    return HttpResponse(json.dumps(success))

def get_user(request):
    data = request.COOKIES
    if 'token' in data:
        valid = auth.valid_user(data['token'])
        if(valid):
            user = auth.get_user_info(data['token'])
            success = {'success':valid, 'token':user.email}
            response = HttpResponse(json.dumps(success))
            response.set_cookie('token',user)
            return response
        else:
            success = {'success':valid}
            return HttpResponse(json.dumps(success))
    else:
        success = {'success':False}
        return HttpResponse(json.dumps(success))

def register(request):
    data = json.loads(request.body)
    auth.register(data['token'])
    user = auth.get_user_info(data['token'])
    success = {'success':True}
    response = HttpResponse(json.dumps(success))
    response.set_cookie('token',user,httponly=True)
    return response

def logout(request):
    success = {'success':True, 'message':'logout success'}
    response = HttpResponse(json.dumps(success))
    response.delete_cookie('token')
    return response
