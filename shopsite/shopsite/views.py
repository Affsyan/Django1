from django.shortcuts import render
from mainapp.models import Product


def index(request):
    title = 'главная'
    products = Product.objects.filter(is_deleted=False, category__is_deleted=False).select_related('category')[:3]

    context = {
        'title': title,
        'products': products,
    }
    return render(request=request, template_name='shopsite/index.html', context=context)


def contacts(request):
    title = 'контакты'

    context = {
        'title': title,
    }
    return render(request=request, template_name='shopsite/contact.html', context=context)
