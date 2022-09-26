# from django.shortcuts import render
# from rest_framework import generics, permissions
# from .serializers import TodoSerializer
# from todo.models import Todo
#
#
# class TodoCompletedList(generics.ListAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         user = self.request.user
#         return Todo.objects.filter(user=user, date_completed__isnull=False).order_by('-date_completed')
