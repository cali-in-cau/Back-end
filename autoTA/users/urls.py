from django.urls import path
from . import views

urlpatterns = [
    path('favorite/add/<str:stock_code>',views.add_favorite),
    path('favorite/delete/<str:stock_code>',views.delete_favorite),
    path('favorites',views.get_favorites),
    path('get_user',views.get_user),
    path('register',views.register),
    path('logout',views.logout)
]