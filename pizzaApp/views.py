# pizzaApp/views.py

from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'main/index.html', context)

def category_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()

    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products': products,
    }
    return render(request, 'main/category.html', context)
