from django.contrib import admin

from .models import Customer, LineItem, Order, Product


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(LineItem)
class LineItemAdmin(admin.ModelAdmin):
    pass
