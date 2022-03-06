from rest_framework import serializers
from .models import RisingStock, NewsOfRisingStock


class StockSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%-m월 %-d일 %H:%M:%S")
    class Meta:
        model = RisingStock
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsOfRisingStock
        fields = ['id', 'title', 'url', 'written_at']
