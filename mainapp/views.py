from django.shortcuts import render
from django.http import HttpResponse
from .models import Novelty


# Create your views here.

def news(request):
    news = Novelty.objects.all()

    return render(request, 'mainapp/news.html', {"news": news, "title": 'Список новостей'})
