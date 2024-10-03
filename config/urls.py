from django.contrib import admin
from django.urls import path, include

from catalog.views import products_list

urlpatterns = [
    path("", products_list, name="products_list"),
    path("admin/", admin.site.urls),
    path("", include("catalog.urls", namespace="catalog")),
]
