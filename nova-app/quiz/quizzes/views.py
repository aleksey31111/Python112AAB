from django.shortcuts import render
from django.http import JsonResponse

from .models import Quiz
from django.views.generic import ListView

from questions.models import Question, Answer
from results.models import Result


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
        for a in q.get_answers():
            answer.append(a.text)
        questions.append({str(q): answer})
    return JsonResponse({
        'data': questions,
        'time': quiz.time
    })

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def save_quiz_view(request, pk):
    if is_ajax(request):
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key:', k)
            question = Question.objects.get(text=k)
            questions.append(question)
        print(questions)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text
                results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})
        score_ = score * multiplier
        Result.objects.create(quiz=quiz, user=user, score=score_)

        if score_ > quiz.required_score_to_pass:
            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'results': results})


# from django.shortcuts import render
# from .models import Quiz
# from django.views.generic import ListView
# from django.http import JsonResponse
# from questions.models import Question, Answer
# from results.models import Result
#
#
# class QuizListView(ListView):
#     model = Quiz
#     template_name = 'quizzes/main.html'
#
#
# def quiz_view(request, pk):
#     quiz = Quiz.objects.get(pk=pk)
#     return render(request, 'quizzes/quiz.html', {'obj': quiz})
