from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.text import slugify


class User(AbstractUser):
    "User Model custom"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('account:profile-detail-view', args=[self.username])
    