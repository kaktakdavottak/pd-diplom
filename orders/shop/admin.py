from django.contrib import admin
from .models import Shop
from products.admin import CategoryInline


class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'filename']
    search_fields = ['name']
    ordering = ['id']
    inlines = [
        CategoryInline,
    ]


admin.site.register(Shop, ShopAdmin)

