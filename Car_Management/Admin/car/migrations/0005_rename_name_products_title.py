# Generated by Django 4.2 on 2023-04-17 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("car", "0004_rename_title_products_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="products",
            old_name="name",
            new_name="title",
        ),
    ]