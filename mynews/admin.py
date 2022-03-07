from django.contrib import admin
from .models import Keyword, NewsOfKeyword


class KeywordAdmin(admin.ModelAdmin):
    search_fields = ['owner__id']


class NewsAdmin(admin.ModelAdmin):
    search_fields = ['keyword__keyword']


admin.site.register(Keyword, KeywordAdmin)
admin.site.register(NewsOfKeyword, NewsAdmin)