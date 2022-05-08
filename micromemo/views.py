from django.shortcuts import render,redirect
from django.views.generic import TemplateView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from django.utils import timezone
from django.views import View
from django.http import HttpResponseRedirect
from requests import request
from .models import Directory,Document
from .forms import  DocumentForm,DirectoryForm,ContactForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail


# Create your views here.

def indexpage(request):
    return render(request,"index.html")

def complete(request):
    return render(request, 'complete.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            recipients = [settings.EMAIL_HOST_USER]

            send_message = subject+"\n"+sender+"\n"+message

            try:
                send_mail('URLmemoのお問い合わせ', send_message, "urlmemo2022@gmail.com", recipients)
            except BadHeaderError:
                return HttpResponse('無効なヘッダーが見つかりました。')
            return redirect('complete')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


@login_required
def frontpage(request):
    posts = Directory.objects.all()
    user = request.user

    if request.method == "POST":
        forms = DirectoryForm(request.POST)

        if forms.is_valid():
            directory = forms.save(commit=False)
            directory.posts = posts
            directory.create_user = user
            directory.save()

            return redirect("/index/frontpage")
    else:
        forms = DirectoryForm()
    
    count = 0
    for post in posts:
        if user.id == post.create_user.id:
            count += 1

    return render(request,"frontpage.html",{"posts":posts, "forms":forms, "count":count})

def post_detail(request,id):
    post = Directory.objects.get(id=id)

    if request.method == "POST":
        form = DocumentForm(request.POST)

        if form.is_valid():
            document = form.save(commit=False)
            document.post = post
            document.save()

            return redirect("post_detail",id=post.id)
    else:
        form = DocumentForm()

    return render(request,"post_detail.html",{"post":post, "form":form})

class DocumentUpdateView(UpdateView):
    template_name = 'document_update.html'
    model = Document
    fields = ( 'title', 'url' ,'comment',)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'id': self.object.post.id})

    def form_valid(self, form):
        document = form.save(commit=False)
        document.updated_at = timezone.now()
        document.save()
        return super().form_valid(form)


class DocumentDeleteView(DeleteView):
    template_name = 'document_delete.html'
    model = Document
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'id': self.object.post.id})


class DirectoryUpdateView(UpdateView):
    template_name = "directory_update.html"
    model = Directory
    fields = ('title','comment')

    def get_success_url(self):
        return reverse('frontpage')

    def form_valid(self, form):
        directory = form.save(commit=False)
        directory.updated_at = timezone.now()
        directory.save()
        return super().form_valid(form)

class DirectoryDeleteView(DeleteView):
    template_name = "directory_delete.html"
    model = Directory

    def delete(self):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse_lazy('frontpage')
