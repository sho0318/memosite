from multiprocessing import parent_process
import re
from django import forms
from django.db import models
from django.template.defaultfilters import slugify
import uuid
import sys
sys.path.append('../')
from accounts.models import CustomUser as User


class Directory(models.Model):
    create_user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=225,unique=False)
    comment = models.TextField(null=True,blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)

    # def clean_title(self):
    #     value = self.title
    #     if not re.match(r'^[A-Za-z0-9_\-\.]+$', value):
    #         raise forms.ValidationError(u'半角英数字のみを使用してください。')
    #     return forms.CharField.clean(self, value)

    # def get_absolute_url(self):
    #     return reverse('article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new

        return super().save(*args, **kwargs)

class Document(models.Model):
    post = models.ForeignKey(Directory, related_name="documents", on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    url = models.URLField(null=True,blank=True)
    comment = models.TextField(null=True,blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)