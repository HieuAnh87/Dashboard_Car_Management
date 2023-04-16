from django.db import models
from django.utils.safestring import mark_safe
from shortuuid.django_fields import ShortUUIDField
from allauth.account.utils import user_pk_to_url_str

# Create your models here.

rating_choice = [
    (0, 'Select'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
]


def product_directory_path(instance, filename):
    return 'products/{0}'.format(filename)


class Customer(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='cus', alphabet="abcdefgh12345")

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, default='123 Street')
    contact = models.CharField(max_length=100, default='0123456789')

    class Meta:
        verbose_name_plural = 'Customer'


class Supplier(models.Model):
    sid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='sup', alphabet="abcdefgh12345")

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, default='123 Street')
    contact = models.CharField(max_length=100, default='0123456789')

    class Meta:
        verbose_name_plural = 'Supplier'


class Products(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='prd', alphabet="abcdefgh12345")

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=product_directory_path)
    description = models.TextField(null=True, blank=True, default='This is the product')

    price = models.DecimalField(max_digits=65, decimal_places=2, default="1.99")

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

    def __str__(self):
        return self.title


class Car(models.Model):
    carid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='car', alphabet="abcdefgh12345")

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    name = models.CharField(max_length=100, null=True, blank=True)
    license = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, default='Bejing x7', null=True, blank=True)
    description = models.TextField(null=True, blank=True, default='This is the product')

    class Meta:
        verbose_name_plural = 'Car'

    def __str__(self):
        return self.car_name
