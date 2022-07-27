# from django.shortcuts import render
# from django.views.generic import ListView, DetailView
# from .models import *
#
# menu = [
#     {'title': 'Add art', 'url_name': 'index'},
#     {'title': 'Enter', 'url_name':'index'},
# ]
# class BlogHome(ListView):
#     model = Blog
#     template_name = 'blog/index.html'
#     context_object_name = 'posts'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Главная страница'
#         context['menu'] = menu
#         return context
#
# class ShowPost(DetailView):
#     model = Blog
#     template_name = 'blog/post.html'
#     slug_url_kwarg = 'post_slug'
#     context_object_name = 'post'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = context['post']
#         context['menu'] = menu
#         return context
#
# class BlogCategory(ListView):
#
#     def get_queryset(self):
#         return

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from .utils import *


menu = [
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Войти', 'url_name': 'index'},
]


class BlogHome(DataMixin, ListView):
    model = Blog
    template_name = "blog/index.html"
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Главная страница'
        # context['cat_selected'] = 0
        # context['menu'] = menu
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) +list(c_def.items()))
        # return context

    def get_queryset(self):
        return Blog.objects.filter(is_published=True).select_related('cat')


class ShowPost(DataMixin, DetailView):
    model = Blog
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = context['post']
        # context['menu'] = menu
        # return context
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class BlogCategory(DataMixin, ListView):
    model = Blog
    template_name = "blog/index.html"
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Blog.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        # context['cat_selected'] = context['posts'][0].cat_id
        # context['menu'] = menu
        # return context
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - '+str(c.name), cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'blog/addpage.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('index')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Добавление статьи'
        # context['menu'] = menu
        # return context
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))