from django.db import models
from django.contrib.auth.models import User

import uuid

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    email = models.CharField(max_length=50, blank=True)
    post_image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    datecreated = models.DateTimeField(auto_now_add=True)
    rndid = models.CharField(
        max_length=100, default=uuid.uuid4, editable=False, null=True, blank=True
    )
    randurl = models.CharField(
        max_length=100, default=uuid.uuid4, editable=False, null=True, blank=True
    )

    def __str__(self):
        return self.title + '|' + self.user

    class Meta:
        ordering = ["datecreated"]
