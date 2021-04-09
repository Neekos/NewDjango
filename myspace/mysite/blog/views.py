from django.shortcuts import render
from django.http import HttpResponse

# form .models import *

# Create your views here.

def index(request):
	return render(request, 'blog/index.html', {'title':'Главная страница'})