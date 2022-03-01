from django.contrib import admin
from .models import *


class StockAdmin(admin.ModelAdmin):
    search_fields = ['code', 'name', 'ratio']

class NewsAdmin(admin.ModelAdmin):
    search_fields = ['title']


admin.site.register(RisingStock, StockAdmin)
admin.site.register(NewsOfRisingStock, NewsAdmin)