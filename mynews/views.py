from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class KeywordListApi(APIView):
    def get(self, request):
        queryset = Keyword.objects.all()
        serializer = KeywordSerializer(queryset, many=True)
        return Response(serializer.data)


class NewsListApi(APIView):
    def get(self, request, keyword):
        newslist = NewsOfKeyword.objects.filter(keyword_id=keyword)
        serializer = NewsSerializer(newslist, many=True)
        return Response(serializer.data)
