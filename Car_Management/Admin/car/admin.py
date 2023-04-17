from django.contrib import admin

from .models import Products, Car, Customer, Supplier, Report, ProductImages


class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pid', 'title', 'product_image', 'price', 'cost_price', 'description', 'type',
                    'stock_count', 'status', 'in_stock']
    inlines = [ProductImagesAdmin]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cid', 'name', 'address', 'contact']


class CarAdmin(admin.ModelAdmin):
    list_display = ['carid', 'name', 'customer', 'license', 'type', 'description']


class ReportAdmin(admin.ModelAdmin):
    list_display = ['rid', 'user_created', 'report_date', 'report_type']


# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Products, ProductAdmin)
admin.site.register(Supplier)
admin.site.register(Report, ReportAdmin)
