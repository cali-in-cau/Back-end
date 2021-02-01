from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('search/',views.search_stock, name='search'),
    path('save_stocks_data/',views.save_stocks_data),
    path('delete_stocks_data/',views.delete_stocks_data),
    path('data/<str:stock_code>',views.show_stock_graph),
]