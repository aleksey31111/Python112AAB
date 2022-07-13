from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required


from .forms import TodoForm
from .models import Todo


def home(request):
    return render(request, 'todo/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html',
                      {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')

            except IntegrityError:
                return render(request, 'todo/signupuser.html',
                              {'form': UserCreationForm(), 'error': 'Такое имя '
                                                'пользователя уже существует. Задайте Другое'})
        else:
            return render(request, 'todo/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Пароли не Совпадают.'})

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def currenttodos(request):
    todos = Todo.objects.filter(user=request.user, date_completed__isnull=True)
    return render(request, 'todo/currenttodos.html', {'todos': todos})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(),
                                                            'error': 'Неверные данные'})
        else:
            login(request, user)
            return redirect('currenttodos')


def createtodo(request):
    if request.method =='GET':
        return render(request, 'todo/createtodo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect("curenttodos")
        except ValueError:
            return redirect(request, 'todo/createtodo.html', {'form': TodoForm(),
                                                              'error': 'Переданы неверные данныеюПопр еще раз'})

def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/viewtodo.html', {'todo': todo,
                                                  'form': form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/viewtodo.html', {'todo': todo,

                                             'form': form, 'erreo': 'Not correct Data'})

@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.date_completed = timezone.now()
        todo.save()
        return redirect('currenttodos')

@ login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    todo.date_completed = timezone.now()
    todo.delete()
    return redirect('currenttodos')

@login_required
def completedtodo(request):
    todos = Todo.objects.\
        filter(user=request.user, date_completed__isnull=False).\
        order_by('-date_completed')
    return render(request, 'todo/completedtodo')


