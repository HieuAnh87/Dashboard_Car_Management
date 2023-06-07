from django.contrib import admin

from .models import Products, Customer, Supplier, ProductImages, CartOrderItems, CartOrder, Order, Invoice, \
    StatisticsProducts


class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pid', 'title', 'product_image', 'category', 'supplier', 'price', 'cost_price', 'description',
                    'stock_count', 'status', 'in_stock']
    inlines = [ProductImagesAdmin]


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['sid', 'name', 'email', 'supplier_image', 'address', 'contact']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cid', 'name', 'address', 'contact']


class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['total_price']


class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['cid', 'user', 'product', 'quantity', 'price']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['oid', 'grand_total', 'tax', 'total_price', 'date_created']


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['iid', 'prod', 'date_created', 'customer', 'order', 'user']


class StatisticAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity_sold', 'total_revenue']


# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Products, ProductAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(StatisticsProducts, StatisticAdmin)
