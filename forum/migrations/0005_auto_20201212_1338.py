# Generated by Django 3.1.3 on 2020-12-12 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0004_auto_20201212_1015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discussion',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterModelOptions(
            name='forum',
            options={'ordering': ['-created_on']},
        ),
        migrations.RenameField(
            model_name='discussion',
            old_name='date_responded',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='forum',
            old_name='date_created',
            new_name='created_on',
        ),
        migrations.RemoveField(
            model_name='discussion',
            name='forum',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='name',
        ),
        migrations.AddField(
            model_name='discussion',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='discussion',
            name='name',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='discussion',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='forum.forum'),
        ),
        migrations.AddField(
            model_name='forum',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forum_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='forum',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='discuss',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='forum',
            name='topic',
            field=models.CharField(max_length=300, null=True),
        ),
    ]