from django.urls import path
from mi.views import *
app_name = "Anything"

urlpatterns = [
    path("captain/",captain)
]