from django.contrib.auth import views as auth_views
from django.urls import path,include
from .views import SignUpView,HomeView

app_name = 'memosite'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('home/', HomeView.as_view(), name="home"),
]