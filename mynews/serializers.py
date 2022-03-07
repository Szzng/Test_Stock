from rest_framework import serializers
from .models import Keyword, NewsOfKeyword


class KeywordSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%-m월 %-d일 %H:%M:%S")
    class Meta:
        model = Keyword
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsOfKeyword
        fields = ['id', 'title', 'url', 'written_at']
