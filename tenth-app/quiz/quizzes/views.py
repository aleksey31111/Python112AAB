from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse


class QuizListView(ListView):
    model = Quiz
    template_name = 'quizzes/main.html'


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quizzes/quiz.html', {'obj': quiz})


def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answer = []
        for a in q.get_answer():
            answer.append(a.text)
        questions.append({str(q): answer})
    return JsonResponse({
        'data': questions,
        'time': quiz.time
    })
