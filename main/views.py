from django.http import HttpResponse
from django.shortcuts import render

from main.models import Category, Product


def index_page(request):
    categories = Category.objects.all()
    return render(request, 'main/index.html', {'categories': categories})


#SELECT, INSERT, UPDATE, DELETE
#TODO: сделать список продуктов
#TODO: авторизация
#TODO: фильтрация, поиск, пагинация
#TODO: корзина
#TODO: заказы
#TODO: отправка песен
#TODO: деплой
#TODO: верстка










