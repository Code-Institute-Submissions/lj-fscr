# Generated by Django 3.1.3 on 2021-01-30 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_auto_20210120_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
