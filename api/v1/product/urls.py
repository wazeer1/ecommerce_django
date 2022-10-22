from django.urls import path, re_path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from . import views

app_name = "api_v1_product"


urlpatterns = [
    re_path(r'^products/$', views.products),
    re_path(r'^categories/$', views.categories),
    re_path(r'^categories/products/(?P<pk>.*)/$', views.categorie_products),
    re_path(r'^add/cart/(?P<pk>.*)/$', views.add_to_category),
    re_path(r'^cart/products/$', views.view_cart_product),
]