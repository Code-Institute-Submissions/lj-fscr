# Generated by Django 3.1.3 on 2020-12-12 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0009_auto_20201212_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(blank=True, max_length=1000)),
                ('created_on', models.DateField(auto_now_add=True, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='forum',
            old_name='date_created',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='forum',
            old_name='description',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='forum',
            old_name='topic',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='email',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='link',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='name',
        ),
        migrations.AddField(
            model_name='forum',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='forum',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forum_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Discussion',
        ),
        migrations.AddField(
            model_name='comment',
            name='forum',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='forum.forum'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]