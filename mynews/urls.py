from django.urls import path
from . import views

app_name = 'api/mynews'

urlpatterns = [
    path('', views.KeywordListApi.as_view(), name='keyword_list'),
    path('<str:keyword>/', views.NewsListApi.as_view(), name='news_list'),
]