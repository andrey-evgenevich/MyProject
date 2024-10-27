from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
# from articles.models import Article


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "photo", "category", "price", "date_create", "date_change")
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "photo", "category", "price", "date_create", "date_change")
    success_url = reverse_lazy('catalog:products_list')


class ProductDeleteView(DeleteView):
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
