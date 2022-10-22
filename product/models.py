from pydoc import describe
from pyexpat import model
from tabnanny import verbose
from unicodedata import category
import uuid
from django.db import models
from main.models import BaseModel

# Create your models here.

class Category(BaseModel):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 255,blank = True,null = True)

    class Meta:
        db_table = 'product_category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(BaseModel):
    # id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 255,blank=True,null = True)
    description = models.TextField()
    category = models.ForeignKey("product.Category",on_delete = models.CASCADE,blank = True,null = True)
    price = models.IntegerField(blank = True,null=True)
    offer = models.IntegerField(blank=True,null = True)
    offer_price = models.IntegerField(blank = True,null = True)
    class Meta:
        db_table = 'product_product'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

