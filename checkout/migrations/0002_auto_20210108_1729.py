# Generated by Django 3.1.3 on 2021-01-08 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='progorderlineitem',
            old_name='lineitem_total',
            new_name='proglineitem_total',
        ),
    ]
