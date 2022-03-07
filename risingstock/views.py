from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class StockListApi(APIView):
    def get(self, request):
        queryset = RisingStock.objects.all()
        serializer = StockSerializer(queryset, many=True)
        return Response(serializer.data)


class NewsListApi(APIView):
    def get(self, request, code):
        newslist = NewsOfRisingStock.objects.filter(code_id=code)
        serializer = NewsSerializer(newslist, many=True)
        return Response(serializer.data)
