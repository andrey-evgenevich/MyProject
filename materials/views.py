from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from materials.models import Materials
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class MaterialsListView(ListView):
    model = Materials


class MaterialsDetailView(DetailView):
    model = Materials


class MaterialsCreateView(CreateView):
    model = Materials
    fields = ("name", "slug", "content", "photo", "date_create", "is_published", "views_count")
    success_url = reverse_lazy('materials:materials_list')


class MaterialsUpdateView(UpdateView):
    model = Materials
    fields = ("name", "slug", "content", "photo", "date_create", "is_published", "views_count")
    success_url = reverse_lazy('materials:materials_list')


class MaterialsDeleteView(DeleteView):
    model = Materials
    success_url = reverse_lazy('materials:materials_list')
