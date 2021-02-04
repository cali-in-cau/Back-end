"""autoTA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users.views import LoginView, SuccessView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('back/accounts/',include('allauth.urls')),
    path('back/users/',include('users.urls')),
    path('back/stocks/',include('stocks.urls')),
    path('back/transactions/',include('transactions.urls')),
    path('back/login/', LoginView),
    path("back/success/", SuccessView),
    #path('back/news/',include('news.urls')),
]
