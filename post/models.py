from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Post(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    likes = models.PositiveIntegerField(default=0)
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def like_a_post(self):
        self.likes += 1
        self.save()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
