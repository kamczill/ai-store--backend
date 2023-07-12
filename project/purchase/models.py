from django.db import models
from products.models import Product
from user.models import User
# Create your models here.
class Purchase(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     product = models.ForeignKey(Product, on_delete=models.CASCADE)
     purchase_timestamp = models.DateTimeField(auto_now_add=True)