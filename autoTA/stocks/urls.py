from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('search/',views.search_stock, name='search'),
    path('save_all/',views.save_stocks),
    path('delete_all/',views.delete_stocks),
    path('graph/<str:stock_code>',views.stock_graph),
]