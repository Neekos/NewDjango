from django.urls import path
from .views import *


urlpatterns = [
	path('', index),
	path('blog', index),
	path('about', about),
	path('photo', photo),
	path('work', work),

]