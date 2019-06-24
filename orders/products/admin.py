from django.contrib import admin
from .models import Category


class CategoryInline(admin.TabularInline):
    model = Category.shops.through
    extra = 1
    exclude = ['shops']
    verbose_name = 'Категория в магазине'
    verbose_name_plural = 'Категории в магазине'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [
        CategoryInline,
    ]
    exclude = ['shops']


admin.site.register(Category, CategoryAdmin)

