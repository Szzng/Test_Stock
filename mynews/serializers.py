from rest_framework import serializers
from .models import Keyword, NewsOfKeyword


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsOfKeyword
        fields = ['id', 'title', 'url', 'written_at']
