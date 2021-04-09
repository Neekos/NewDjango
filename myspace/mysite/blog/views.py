from django.shortcuts import render
from django.http import HttpResponse

form .models import *

# Create your views here.

def index():
	return render(request, 'blog/index.html')