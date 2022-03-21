from re import search
from django.contrib import admin
from .models import Realtor
# Register your models here.

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date','is_mvp')
    list_display_link = ('id', 'name')
    list_editable = ('is_mvp',)
    search_field = ('name',)
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)