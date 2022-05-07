from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password1","password2"]


class UserChangeForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',            
        ]

    def __init__(self, email=None, username=None, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        # ユーザーの更新前情報をフォームに挿入
        if email:
            self.fields['email'].widget.attrs['value'] = email
        if username:
            self.fields['username'].widget.attrs['value'] = username

    def update(self, user):
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.save()