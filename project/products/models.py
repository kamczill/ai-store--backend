from django.utils import timezone
from django.db import models
import uuid
from user.models import User
# Create your models here.
class Product(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)

    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    description = models.CharField(unique=True)
    cover = models.FileField(upload_to='files/')
    date_created = models.DateTimeField(default=timezone.now)
    net_price = models.DecimalField(max_digits=6, decimal_places=2)
