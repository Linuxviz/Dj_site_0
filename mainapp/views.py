from django.shortcuts import render
from django.http import HttpResponse
from .models import Novelty, Category


# Create your views here.

def news(request):
    news = Novelty.objects.all()
    #category = Category.objects.all()

    context = {
        "news": news,
        "title": 'Список новостей',
        #"categories": category
    }

    return render(request, 'mainapp/news.html', context)


def view_category(request, index):
    news = Novelty.objects.filter(category_id=index)
    category = Category.objects.get(pk=index)
    context = {
        "news": news,
        "category": category
    }
    return render(request, 'mainapp/category.html', context)
