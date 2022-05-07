from re import template
from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.views import  LogoutView
from django.views import View
from django.views.generic import FormView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import render
from .forms import SignUpForm,UserChangeForm
from requests import request
from .models import CustomUser


class LogoutComplete(LogoutView,View):
    template_name = 'logout_complete.html'

    def get_seccess_url(self):
        return reverse_lazy("index")

class Logout(TemplateView):
    template_name = 'logout.html'

class HomeView(TemplateView):
    template_name = "home.html"

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "signup.html"
    success_url = reverse_lazy("frontpage")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user,backend='django.contrib.auth.backends.ModelBackend')
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

class AccountView(TemplateView):
    template_name="account.html"

class UserChangeView(LoginRequiredMixin, FormView):
    template_name = 'change.html'
    form_class = UserChangeForm
    success_url = reverse_lazy("account")

    def form_valid(self, form):
        #formのupdateメソッドにログインユーザーを渡して更新
        form.update(user=self.request.user)
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # 更新前のユーザー情報をkwargsとして渡す
        kwargs.update({
            'email' : self.request.user.email,
            'username' : self.request.user.username,
        })
        return kwargs


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.username == self.kwargs['username'] or user.is_superuser

class UserDeleteView(OnlyYouMixin, DeleteView):
    template_name = "delete.html"
    success_url = reverse_lazy("index")
    model = CustomUser
    slug_field = 'username'
    slug_url_kwarg = 'username'