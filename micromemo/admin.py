from django.contrib import admin
from .models import Document,Directory

# Register your models here.
class DirectoryAdmin(admin.ModelAdmin):
    fields = ['create_user', 'title', 'comment', 'posted_date', 'id']

class DocumentAdmin(admin.ModelAdmin):
    fields = ['post','title','url','comment','posted_date','id']

admin.site.register(Document,DocumentAdmin)
admin.site.register(Directory,DirectoryAdmin)