from pyexpat import model
from django.db import models
from api.v1.main.functions import get_auto_id
from main.models import BaseModel
from main.middlewares import RequestMiddleware
# Create your models here.


class Cart(BaseModel):
    user = models.ForeignKey('accounts.Profile',on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=255,blank=True,null=True)
    total_cart_price=models.CharField(max_length = 255,blank = True,null = True)
    def save(self, *args, **kwargs):        
        if self._state.adding:
            # First we need create an instance of that and later get the current_request assigned
            request = RequestMiddleware(get_response=None)
            request = request.thread_local.current_request

            self.auto_id = get_auto_id(Cart)
            self.creator = request.user.pk
            self.updater = request.user.pk
        
        super(Cart, self).save(*args, **kwargs)
    class Meta:
        db_table = 'user_cart'
        verbose_name = 'cart'
        verbose_name_plural = 'carts'
    def __str__(self):
        return self.name

class CartProducts(models.Model):
    cart = models.ForeignKey('cart.Cart',on_delete=models.CASCADE,blank=True,null=True)
    product =models.ForeignKey('product.Product',on_delete=models.CASCADE,blank=True,null=True)
    product_count = models.IntegerField(max_length = 255,blank=True,null=True)
    product_total_price = models.IntegerField(max_length = 255,blank=True,null=True)
    class Meta:
        db_table = 'cart_cartproducts'
        verbose_name='cart product'
        verbose_name_plural='cart_products'
    def __str__(self):
        return self.product.name

