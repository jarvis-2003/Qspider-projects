from django.urls import path
from musicplayer.views import *
app_name = 'musicplayer'

urlpatterns = [
    path('home/', home , name = 'home'),
]