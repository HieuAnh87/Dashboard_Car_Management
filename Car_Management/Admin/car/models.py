from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe
from shortuuid.django_fields import ShortUUIDField

# Create your models here.

rating_choice = [
    (0, 'Select'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
]

REPORT_TYPE = [
    ('inventory report', 'Inventory report'),
    ('sales report', 'Sales report'),
]

CATEGORY_TYPE = [
    ('car interior', 'Car Interior'),
    ('car exterior', 'Car Exterior'),
    ('car accessories', 'Car Accessories'),
    ('car care services', 'Car Care Services'),
]


def product_directory_path(instance, filename):
    return 'products/{0}'.format(filename)


class Customer(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='cus', alphabet="abcdefgh12345")

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, default='123 Street')
    city = models.CharField(max_length=100, default='City')
    district = models.CharField(max_length=100, default='district')
    ward = models.CharField(max_length=100, default='district')
    contact = models.CharField(max_length=100, default='0123456789')

    class Meta:
        verbose_name_plural = 'Customer'

    def __str__(self):
        return self.name


class Supplier(models.Model):
    sid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='sup', alphabet="abcdefgh12345")

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, default='123 Street')
    contact = models.CharField(max_length=100, default='0123456789')

    class Meta:
        verbose_name_plural = 'Supplier'

    def __str__(self):
        return self.name


class Products(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='prd', alphabet="abcdefgh12345")

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=product_directory_path)
    category = models.CharField(choices=CATEGORY_TYPE, max_length=100, default='car interior')
    description = models.TextField(null=True, blank=True, default='This is the product')

    cost_price = models.DecimalField(max_digits=65, decimal_places=2, default="1.99")
    price = models.DecimalField(max_digits=65, decimal_places=2, default="1.99")
    old_price = models.DecimalField(max_digits=65, decimal_places=2, default="1.99")

    type = models.CharField(max_length=100, default='This is the product', null=True, blank=True)
    stock_count = models.CharField(max_length=100, default='8', null=True, blank=True)

    status = models.BooleanField(default=True)  # active or not
    in_stock = models.BooleanField(default=True)  # in stock or not

    class Meta:
        verbose_name_plural = 'Product'

    def product_image(self):
        if self.image:
            return mark_safe('<img src="%s" width="50" height="50" />' % self.image.url)
        else:
            return 'No Image Found'

    def profit(self):
        return self.price - self.cost_price

    def get_percentage(self):
        new_price = ((self.old_price - self.price) / self.old_price) * 100
        return int(new_price)

    def __str__(self):
        return self.title


class ProductImages(models.Model):
    image = models.ImageField(upload_to="product-images", default="product.png")
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, related_name="p_images")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Images'


class Receipt(models.Model):
    rid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='rec', alphabet="abcdefgh12345")

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True, default='This is the product')

    class Meta:
        verbose_name_plural = 'Receipt'

    def __str__(self):
        return self.rid


class Report(models.Model):
    rid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='rep', alphabet="abcdefgh12345")

    user_created = models.ForeignKey(User, on_delete=models.CASCADE)

    report_text = models.TextField(null=True, blank=True, default='This is a report')
    report_date = models.DateTimeField(auto_now_add=True)
    report_type = models.CharField(choices=REPORT_TYPE, max_length=100, default='inventory report')

    class Meta:
        verbose_name_plural = 'Report'

    def __str__(self):
        return self.rid


class CartOrder(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='car', alphabet="abcdefgh12345")

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_orders')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='cart_orders')
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=65, decimal_places=2, default="1.99")

    class Meta:
        verbose_name_plural = 'CartOrder'

    def __str__(self):
        return self.cid

    def get_price(self):
        return int(self.quantity) * self.product.price


class CartOrderItems(models.Model):
    cart_order = models.ForeignKey(CartOrder, on_delete=models.CASCADE, related_name='cart_order_items')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_order_items')

    grand_total = models.DecimalField(max_digits=65, decimal_places=2, default="1.99")
    tax = models.DecimalField(max_digits=65, decimal_places=2, default="1.99")
    total_price = models.DecimalField(max_digits=65, decimal_places=2, default="1.99")

    class Meta:
        verbose_name_plural = 'CartOrderItems'

    def __str__(self):
        return self.cart_order.cid


class Order(models.Model):
    oid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='ord', alphabet="abcdefgh12345")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    cart_order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    cart_order_items = models.ForeignKey(CartOrderItems, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return self.oid
