from django.urls import path
from . import views

app_name = 'risingstock'

urlpatterns = [
    path('', views.StockIndexView.as_view(), name='index'),
    path('<str:code>/', views.StockDetailView.as_view(), name='detail'),
]
