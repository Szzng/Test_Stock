from django.urls import path
from . import views

app_name = 'api/risingstock'

urlpatterns = [
    path('', views.StockListApi.as_view(), name='stock_list'),
    path('<str:code>/', views.NewsListApi.as_view(), name='news_list'),
]