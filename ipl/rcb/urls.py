from django.urls import path
from rcb.views import *
app_name = "Anything"

urlpatterns = [
    path("captain/",captain)
]