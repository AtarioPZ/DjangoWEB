from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path("", views.index, name='App1'),
    path("notIndex", views.notIndex, name='notindex')
]