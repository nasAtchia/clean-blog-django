from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    slug = models.SlugField(unique=True, max_length=255)
