# Generated by Django 3.1.3 on 2020-12-14 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0023_auto_20201214_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forum_threads', to=settings.AUTH_USER_MODEL),
        ),
    ]
