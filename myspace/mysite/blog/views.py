from django.shortcuts import render
from django.http import HttpResponse

# form .models import *

# Create your views here.

def index(request):
	return render(request, 'blog/main.html', {'title':'Главная страница'})

def about(request):
	return render(request, 'blog/about.html', {'title':'Обо мне'})

def photo(request):
	return render(request, 'blog/photo.html', {'title':'Галерея'})

def work(request):
	return render(request, 'blog/work.html', {'title':'Мои работы'})