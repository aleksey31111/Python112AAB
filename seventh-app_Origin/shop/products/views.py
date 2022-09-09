from django.shortcuts import render, redirect
from products.models import ProductCategory, Product, Basket
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        'title': 'Market Place'
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    context = {
        'title': 'Market Place - Каталог',
        'categories': ProductCategory.objects.all(),
    }
    if category_id:
        products = Product.objects.all().filter(category_id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 3)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context.update({'products': page_obj})
    return render(request, 'products/products.html', context)


def basket_add(request, product_id):
    current_page = request.META.get("HTTP_REFERER")
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        # basket = Basket(user=request.user, product=product, quantity=1)
        # basket.save()
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return redirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return redirect(current_page)


@login_required(login_url="/users/login/")
def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return redirect(request.META.get("HTTP_REFERER"))

