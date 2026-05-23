from django.contrib import admin
from .models import Guest, Drinks
from django.contrib.auth.models import Group

@admin.register(Guest)
class CategoryAdmin(admin.ModelAdmin):
    """ Отображение гостей и алко в админке """
    list_display = ['fio', 'created_date']
    verbose_name = 'Гость'


@admin.register(Drinks)
class CategoryAdmin(admin.ModelAdmin):
    """ Отображение гостей и алко в админке """
    list_display = ['sort', 'name']
    verbose_name = 'Гость'
    ordering = ['sort']


admin.site.unregister(Group)
