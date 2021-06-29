from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def products(request):
    title = 'продукты'
    products = Product.objects.all()[:3]
    links_menu = ProductCategory.objects.all().order_by('name')
    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products,
    }
    return render(request=request, template_name='mainapp/products.html', context=context)
