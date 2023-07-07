from django.utils import timezone
from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField()
    cover = models.FileField(upload_to='files/')
    date_created = models.DateTimeField(default=timezone.now)

