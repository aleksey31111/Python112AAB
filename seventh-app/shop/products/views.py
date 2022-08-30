from django.shortcuts import render


def index(request):
    context = {
        'title': 'Market Place'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Market Place - Каталог'
    }
    return render(request, 'products/products.html', context)
