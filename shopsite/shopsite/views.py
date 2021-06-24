from django.shortcuts import render


def index(request):
    title = 'главная'
    context = {
        'title': title
    }
    return render(request=request, template_name='shopsite/index.html', context=context)


def contacts(request):
    title = 'контакты'
    context = {
        'title': title
    }
    return render(request=request, template_name='shopsite/contact.html', context=context)
