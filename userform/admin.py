from django.contrib import admin
from .models import UserEntry 
# Register your models here.

class UserEntryAdmin(admin.ModelAdmin):
    list_display = ( 'uuid', 'header', 'link', 'email')

admin.site.register(UserEntry, UserEntryAdmin)
