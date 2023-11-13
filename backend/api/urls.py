from django.urls import path
from .views import *

urlpatterns=[
    path('',api_home),
    path('cats',api_cats),
    path('create_user',api_create_user)
]