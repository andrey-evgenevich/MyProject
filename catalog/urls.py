from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import HomeTemplateView, ContactsTemplateView, ProductDetailView, ProductListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("products/", ProductListView.as_view(), name="products_list"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("products/<int:pk>", cache_page(60)(ProductDetailView.as_view()), name="products_detail"),
    path("catalog/create", ProductCreateView.as_view(), name="products_create"),
    path("catalog/<int:pk>/update", ProductUpdateView.as_view(), name="products_update"),
    path("catalog/<int:pk>/delete", ProductDeleteView.as_view(), name="products_delete"),
]
