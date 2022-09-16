from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from .models import News
from .serializers import NewsSerializer

from rest_framework.response import Response
from rest_framework.views import APIView


# class NewsAPIView(generics.ListAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer


class NewsAPIView(APIView):
    def get(self, request):
        # return Response({'title': 'Новость 1'})
        lst = News.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        # return Response({'title': 'Новость 2'})
        post_new = News.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            category_id=request.data['category_id']
        )
        return Response({'post': model_to_dict(post_new)})
