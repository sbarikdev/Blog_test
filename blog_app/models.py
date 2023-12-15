from django.db import models
from accounts.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']