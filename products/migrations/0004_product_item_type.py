# Generated by Django 3.1.3 on 2021-01-15 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_item_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='item_type',
            field=models.CharField(blank=True, default='product', max_length=20, null=True),
        ),
    ]
