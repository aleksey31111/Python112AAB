from django.shortcuts import render
from .models import Quiz
from questions.models import Question
from questions.models import Answer

from django.views.generic import ListView


class QuizListView(ListView):
    model = Quiz
    template_name = 'quizzes/main.html'


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quizzes/quiz.html', {'obj': quiz})


class QuestionsListView(ListView):
    model = Question
    template_name = 'quizzes/main.html'

def questions_view(request, pk):
    questions = Question.object.get(pk=pk)



# def test1(request):
#     return render(request, 'quizzes/test1.html')


# def test2(request):
#     return render(request, 'quizzes/test2.html')