from django.contrib import admin
from .models import Category, Product, ProductInfo, Parameter, ProductParameter


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


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ['product', 'model', 'quantity', 'price', 'price_rrc']


class ParameterAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProductParameterAdmin(admin.ModelAdmin):
    list_display = ['product_info', 'parameter', 'value']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductInfo, ProductInfoAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(ProductParameter, ProductParameterAdmin)

