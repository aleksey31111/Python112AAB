from rest_framework import serializers
from todo.models import Todo


class ToDoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    date_completed = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'created', 'date_completed', 'important']


class TodoCompleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ['id']
        read_only_fields = ['id', 'title', 'memo', 'created', 'date_completed', 'important']