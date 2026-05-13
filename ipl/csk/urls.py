from django.urls import path
from csk.views import *
app_name = "Something"
urlpatterns = [
    path('captain/',captain)
]
# print(app_name)