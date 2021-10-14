from django.contrib import admin
from .models import UserEntry, Language 
# Register your models here.

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language', 'shortcut', 'flag')

class UserEntryAdmin(admin.ModelAdmin):
    list_display = ('header', 'link', 'email')

admin.site.register(UserEntry)
admin.site.register(Language, LanguageAdmin)