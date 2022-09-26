from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from .models import News
from .serializers import NewsSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, \
    IsAdminUser


# class NewsAPIView(generics.ListAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer

class NewsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsAPIList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer  # Реализует GET и POST
    permission_classes = (IsAuthenticatedOrReadOnly,)


# class NewsAPIUpdate(generics.UpdateAPIView):
class NewsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer  # Реализует метод PUT
    permission_classes = (IsOwnerOrReadOnly,)


class NewsAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAdminOrReadOnly,)

class NewsAPIView(APIView):
    def get(self, request):
        # return Response({'title': 'Новость 1'})
        n = News.objects.all()
        # lst =
        return Response({'posts': NewsSerializer(n, many=True).data})

    def post(self, request):
        # return Response({'title': 'Новость 2'})
        serializer = NewsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = News.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            category_id=request.data['category_id']
        )
        # return Response({'post': model_to_dict(post_new).data})
        return Response({'post': NewsSerializer(post_new).data})
