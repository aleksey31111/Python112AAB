from django import template
from blog.models import *

register = template.Library()

@egister.inclusion_tag('blog/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.obects.order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}
