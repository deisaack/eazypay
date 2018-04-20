from django.db import models
from django.contrib.postgres.fields import JSONField
import uuid
from django.contrib.auth import get_user_model

User = get_user_model()


class Traffic(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    ip = models.GenericIPAddressField(null=True, blank=True, verbose_name='IP')
    user_agent = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    path = models.TextField(blank=True)

    def __str__(self):
        if not self.user:
            return str(self.ip)
        return self.user.username

class PageRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    page = models.CharField(max_length=100)
    request = models.TextField(blank=True)
    responce = models.TextField(blank=True)
    ip=models.GenericIPAddressField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.page + ' ' +str(self.id)

