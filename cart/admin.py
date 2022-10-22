from django.contrib import admin

from cart.models import Cart, CartProducts

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ('id',)
admin.site.register(Cart,CartAdmin)

admin.site.register(CartProducts)