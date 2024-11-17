from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from catalog.forms import ProductForm
from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
# from articles.models import Article
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        product = form.save()
        product.user = self.request.user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ("name", "description", "photo", "category", "price", "date_create", "date_change")
    success_url = reverse_lazy('catalog:products_list')


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
