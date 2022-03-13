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

    def create(self, request, *args, **kwargs):
        keyword, created = Keyword.objects.get_or_create(keyword=request.data['keyword'])
        keyword.save()
        keyword.owner.add(request.user)
        serializer = KeywordSerializer(keyword)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = NewsOfKeyword.objects.filter(keyword=pk)
        serializer = NewsSerializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        keyword = self.get_object()
        keyword.owner.remove(request.user)
        if keyword.owner.count() == 0:
            keyword.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

