# https://djangocentral.com/building-a-blog-application-with-django/

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Thread(models.Model):
    topic = models.CharField(max_length=200, unique=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               null=True)
    description = models.TextField(null=True)
    created_on = models.DateField(auto_now_add=True, null=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-created_on']  # Default sort

    def __str__(self):
        return self.topic

    # https://stackoverflow.com/questions/45847278/django-use-slugify-for-detail-url
    def save(self, *args, **kwargs):
        self.slug = slugify(self.topic, allow_unicode=True)
        return super(Thread, self).save(*args, **kwargs)


class Reply(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name
                               ='replies', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    body = models.CharField(max_length=300, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Reply {} by {}'.format(self.body, self.user)
