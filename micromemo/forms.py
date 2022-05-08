from django import forms
from .models import Document,Directory

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ["title","url","comment"]

class DirectoryForm(forms.ModelForm):
    class Meta:
        model = Directory
        fields = ["title","comment"]

class ContactForm(forms.Form):
    subject = forms.CharField(label='subject', max_length=100)
    sender = forms.EmailField(label='email', help_text='※ご確認の上、正しく入力してください。')
    message = forms.CharField(label='message', widget=forms.Textarea)
