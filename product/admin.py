from django.contrib import admin

from product.models import Category, Product

# Register your models here.
# class FollowersAdmin(admin.ModelAdmin):
#     list_display = ('id',)
#     ordering = ('date_added',)
# admin.site.register(Followers,FollowersAdmin)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price',)
admin.site.register(Product,ProductAdmin)