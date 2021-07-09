
from django.shortcuts import render
from mainapp.models import Product

from basketapp.models import Basket


def index(request):
    title = 'главная'
    products = Product.objects.all()[:3]
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {
        'title': title,
        'products': products,
        'basket': basket
    }
    return render(request=request, template_name='shopsite/index.html', context=context)


def contacts(request):
    title = 'контакты'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {
        'title': title,
        'basket': basket,
    }
    return render(request=request, template_name='shopsite/contact.html', context=context)
