from django.shortcuts import render
from rest_framework import generics
from .models import News
from .serializers import NewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# class NewsAPIView(generics.ListAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer


class NewsAPIView(APIView):
    def get(self,request):
        lst = News.objects
        return Response({'title': 'Новость 1'})

    def post(self, requests):
        return Response({'title': 'Новость 2'})
