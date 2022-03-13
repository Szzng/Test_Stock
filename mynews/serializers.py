from rest_framework import serializers
from .models import Keyword, NewsOfKeyword


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'
        depth = 1


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsOfKeyword
        fields = ['id', 'title', 'url', 'written_at']
