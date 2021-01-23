from django.contrib import admin
from .models import User, Favorite
# Register your models here.
admin.site.register(User)
admin.site.register(Favorite)