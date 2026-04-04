from django.contrib import admin
from .models import Extension

@admin.register(Extension)
class ExtensionAdmin(admin.ModelAdmin):
    list_display = ('number', 'password') 
    search_fields = ('number',)