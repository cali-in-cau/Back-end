from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('save_stock_data/',views.save_stock_data),
    path('delete_stock_data/',views.delete_stock_data),
]