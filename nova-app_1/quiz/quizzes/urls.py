from django.urls import path
from .views import QuizListView, quiz_view


app_name = 'quizzes'

urlpatterns = [
    path('', QuizListView.as_view(), name="main-view"),
    path('<int:pk>/', quiz_view, name="quiz-view"),

    # Тесты
    # path('quizzes/test1/', views.test1, name='test1'),
    # path('quizzes/test2/', views.test2, name='test2'),
]