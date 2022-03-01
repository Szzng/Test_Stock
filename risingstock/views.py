from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import RisingStock, NewsOfRisingStock


class StockIndexView(ListView):
    model = RisingStock
    template_name = 'risingstock/index.html'


class StockDetailView(DetailView):
    model = RisingStock