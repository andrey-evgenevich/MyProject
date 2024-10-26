from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from materials.models import Materials
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify


class MaterialsListView(ListView):
    model = Materials

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class MaterialsDetailView(DetailView):
    model = Materials

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return object


class MaterialsCreateView(CreateView):
    model = Materials
    fields = ("name", "slug", "content", "photo", "date_create", "is_published", "views_count")
    success_url = reverse_lazy('materials:materials_list')

    def form_valid(self, form):
        if form.is_valid():
            new_material = form.save()
            new_material.slug = slugify(new_material.name)
            new_material.save()
        return super().form_valid(form)


class MaterialsUpdateView(UpdateView):
    model = Materials
    fields = ("name", "slug", "content", "photo", "date_create", "is_published", "views_count")
    # success_url = reverse_lazy('materials:materials_list')

    def get_success_url(self):
        return reverse('materials:view', args=[self.kwargs.get('pk')])


class MaterialsDeleteView(DeleteView):
    model = Materials
    success_url = reverse_lazy('materials:materials_list')
