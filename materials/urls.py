from django.urls import path
from materials.apps import MaterialsConfig
from materials.views import (MaterialsListView, MaterialsDetailView, MaterialsCreateView,
                             MaterialsUpdateView, MaterialsDeleteView)

app_name = MaterialsConfig.name

urlpatterns = [
    path("", MaterialsListView.as_view(), name="materials_list"),
    path("<int:pk>", MaterialsDetailView.as_view(), name="materials_detail"),
    path("create", MaterialsCreateView.as_view(), name="materials_create"),
    path("<int:pk>/update", MaterialsUpdateView.as_view(), name="materials_update"),
    path("<int:pk>/delete", MaterialsDeleteView.as_view(), name="materials_delete"),
]
