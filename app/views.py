from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
from os import listdir, getcwd


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.now()
    msg_time = f'Текущее время: {current_time}'
    return HttpResponse(msg_time)


def workdir_view(request):
    current_directory = listdir(getcwd())
    msg_time = f'В текущей директории содержаться файлы: {current_directory}'
    return HttpResponse(msg_time)
