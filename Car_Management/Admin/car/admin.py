from django.contrib import admin
from .models import Products, Car, Customer, Supplier


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pid', 'title', 'product_image', 'price', 'description', 'price', 'type',
                    'stock_count', 'status', 'in_stock']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cid', 'name', 'address', 'contact']


class CarAdmin(admin.ModelAdmin):
    list_display = ['carid', 'name', 'customer', 'license', 'type', 'description']

# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Products, ProductAdmin)
admin.site.register(Supplier)
