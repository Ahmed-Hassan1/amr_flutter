from django.urls import path
from .views import *

urlpatterns=[
    path('',api_home),
    path('cats',api_cats)
]