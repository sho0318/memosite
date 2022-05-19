from re import template
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path,include
from micromemo.views import frontpage,post_detail,indexpage,DocumentUpdateView,DocumentDeleteView,DirectoryUpdateView,DirectoryDeleteView,contact_view,complete,my_customized_server_error
from accounts.views import SignUpView,HomeView,Logout,LogoutComplete,UserChangeView,AccountView,UserDeleteView

app_name = 'memosite'
handler500 = my_customized_server_error

urlpatterns = [
    path('admin/sho/admin/', admin.site.urls),
    path("index/account/",include('allauth.urls')),
    path("",indexpage),
    path("index/",indexpage,name="index"),
    path("index/frontpage/",frontpage,name="frontpage"),
    path("<uuid:id>/",post_detail,name="post_detail"),
    path('<uuid:id>/update/<uuid:pk>/', DocumentUpdateView.as_view(), name='document_update'),
    path('<uuid:id>/delete/<uuid:pk>/', DocumentDeleteView.as_view(), name='document_delete'),
    path('<uuid:pk>/update',DirectoryUpdateView.as_view(),name="directory_update"),
    path('<uuid:pk>/delete',DirectoryDeleteView.as_view(),name="directory_delete"),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('logout/True/',LogoutComplete.as_view(),name="logout_complete"),
    path('account/',AccountView.as_view(),name="account"),
    path('account/update/',UserChangeView.as_view(),name="change"),
    path('<str:username>/delete/', UserDeleteView.as_view(), name='account_delete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('signup/', SignUpView.as_view(), name="signup"),
    path('home/', HomeView.as_view(), name="home"),

    path('contact',contact_view,name="contact"),
    path('contact/complete/', complete, name='complete'),
]
