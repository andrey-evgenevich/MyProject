from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
# from articles.models import Article
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.services import get_product_from_cache


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return get_product_from_cache(Product)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.views_counter += 1
            self.object.save()
            return self.object
        raise PermissionDenied


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ("name", "description", "photo", "category", "price", "date_create", "date_change")
    success_url = reverse_lazy('catalog:products_list')

    def get_form_class(self):
        """ Получаем форму в зависимости от прав пользователя  """
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.change_category') and user.has_perm('catalog.change_depiction') and user.has_perm(
                'catalog.change_publication'):
            return ProductModeratorForm
        raise PermissionDenied('У вас недостаточно прав для редактирования этого продукта.')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')


class HomeTemplateView(TemplateView):
    template_name = "catalog/home.html"

# def home(request):
#     return render(request, "catalog/home.html")


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

# def contacts(request):
#     return render(request, "catalog/contacts.html")
