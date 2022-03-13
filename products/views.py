from django.http import HttpResponse
from django.shortcuts import render

from .models import Products, Category


def index(req):
    products = Products.objects.all()
    categories = Category.objects.all()

    return render(req, 'products/index.html', {
        'products': products,
        'categories': categories,
        'title': 'Products List'
    })


def category(req, id):
    products = Products.objects.filter(category=id)
    categories = Category.objects.all()

    return render(req, 'products/index.html', {
        'products': products,
        'categories': categories,
        'title': 'Products List'
    })


def product_page(req, id):
    product = Products.objects.get(pk=id)
    products = Products.objects.filter(category=product.category.pk)

    return render(req, 'products/product.html', {
        'product': product,
        'products': products
    })
