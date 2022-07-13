from django.shortcuts import render
from django.views.generic import ListView

from .models import *

menu = [
    {'title': 'Add art', 'url_name': 'index'},
    {'title': 'Enter', 'url_name':'index'}
]
class BlogHome(ListView):
    model = Blog
    template_name = 'blog/index.html'
    contextobject_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        context
