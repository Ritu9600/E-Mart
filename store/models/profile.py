from django.db import models
from .category import Category
from .customer import Customer

class Profile(models.Model):
    last_name = models.CharField(max_length=100)

