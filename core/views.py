from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def products_list(request):
    return render(request, 'products_list.html')


def product(request):
    return render(request, 'product.html')
