from django.contrib import admin
from .models import UserEntry, Language 
# Register your models here.

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language', 'shortcut', 'flag')

class UserEntryAdmin(admin.ModelAdmin):
    list_display = ( 'uuid', 'header', 'link', 'email')
    readonly_fields = ('uuid',)

admin.site.register(UserEntry, UserEntryAdmin)
admin.site.register(Language, LanguageAdmin)