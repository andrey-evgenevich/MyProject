from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "photo", "category", "price", "date_create", "date_change")
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "photo", "category", "price", "date_create", "date_change")
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")
