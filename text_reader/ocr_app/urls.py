from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.button,name="button"),
    path('output/',views.output,name="output"),
]