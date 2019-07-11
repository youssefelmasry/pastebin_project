from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Paste(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='pastebin', blank=True, null=True)
    title = models.CharField(max_length=100, default='Untitled')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    public = models.BooleanField(default=True)
    private = models.BooleanField(default=False)
    sharedWith = models.ManyToManyField(User, blank=True, related_name='shared_with')


    def __str__(self):
        return self.title

# Every user will have an automatically generated token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)