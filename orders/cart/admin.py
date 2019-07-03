from django.contrib import admin
from .models import Order, OrderItem, Contact, Phone, Address


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'dt', 'status']
    search_fields = ['user']
    list_filter = ['user', 'dt', 'status']
    inlines = [OrderItemInline]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


class ContactAdmin(admin.ModelAdmin):
    pass


class PhoneAdmin(admin.ModelAdmin):
    pass


class AddressAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Address, AddressAdmin)

