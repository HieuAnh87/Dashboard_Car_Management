from django.contrib import admin
from .models import Products, Car, Customer, Supplier


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pid', 'title', 'product_image', 'price', 'description', 'price', 'type',
                    'stock_count', 'status', 'in_stock']


# Register your models here.
admin.site.register(Customer)
admin.site.register(Car)
admin.site.register(Products, ProductAdmin)
admin.site.register(Supplier)
