from django.contrib import admin

from .models import Products, Customer, Supplier, Report, ProductImages, CartOrderItems, CartOrder


class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pid', 'title', 'product_image', 'category', 'price', 'cost_price', 'description', 'type',
                    'stock_count', 'status', 'in_stock']
    inlines = [ProductImagesAdmin]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cid', 'name', 'address', 'contact']


class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['total_price']


class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['cid', 'user', 'product', 'quantity', 'price']


class ReportAdmin(admin.ModelAdmin):
    list_display = ['rid', 'user_created', 'report_date', 'report_type']


# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Products, ProductAdmin)
admin.site.register(Supplier)
admin.site.register(Report, ReportAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
