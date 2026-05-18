from django.urls import path
from todolist.views import *
app_name = 'todolist'

urlpatterns = [
    path('home/',home,name='home')
]