from msilib.schema import Directory
from re import template
from django.contrib.auth import views as auth_views
from django.contrib import admin,auth
from django.urls import path,include
from .views import SignUpView,HomeView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('home/', HomeView.as_view(), name="home"),
]