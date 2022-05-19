from django.contrib import admin
from .models import Document,Directory

# Register your models here.
class DirectoryAdmin(admin.ModelAdmin):
    fields = ['create_user', 'title', 'comment']

class DocumentAdmin(admin.ModelAdmin):
    fields = ['post','title','url','comment']

admin.site.register(Document,DocumentAdmin)
admin.site.register(Directory,DirectoryAdmin)