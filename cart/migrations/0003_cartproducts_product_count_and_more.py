# Generated by Django 4.1 on 2022-10-01 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_total_cart_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproducts',
            name='product_count',
            field=models.IntegerField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cartproducts',
            name='product_total_price',
            field=models.IntegerField(blank=True, max_length=255, null=True),
        ),
    ]
