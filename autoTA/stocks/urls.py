from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    #path('search/',views.search_stock, name='search'),
    path('search/<str:keyword>',views.search_stock),
    path('search/<str:stock_code>',views.search_stock_with_code),
    path('save_all/',views.save_stocks),
    path('delete_all/',views.delete_stocks),
    path('graph/',views.stock_graph),
    path('predict/',views.stock_predict),
]