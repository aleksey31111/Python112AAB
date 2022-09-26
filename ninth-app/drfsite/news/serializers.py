from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = News
        fields = '__all__'
#         fields = ('title', 'content', 'time_created', 'time_update', 'is_published', 'category_id')
# ### ПОЛЯ Модули
#     # fields = ('title', 'content', 'time_created', 'time_update',
#     #               'is_published', 'category_id')
#         title = serializers.CharField(max_length=255)
#         content = serializers.CharField()
#         time_created = serializers.DateTimeField(read_only=True)
#         time_update = serializers.DateTimeField(read_only=True)
#         is_published = serializers.BooleanField(default=True)
#         category_id = serializers.IntegerField()
