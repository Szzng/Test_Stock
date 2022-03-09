from rest_framework.response import Response
from rest_framework import viewsets, mixins, status

from .serializers import *


class MyNewsViewSet(mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    serializer_class = KeywordSerializer

    def get_queryset(self):
        return Keyword.objects.filter(owner=self.request.user).order_by('keyword')

    def retrieve(self, request, pk):
        queryset = NewsOfKeyword.objects.filter(keyword=pk)
        serializer = NewsSerializer(queryset, many=True)
        return Response(serializer.data)
