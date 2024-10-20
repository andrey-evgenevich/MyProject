from django.urls import path
from materials.apps import MaterialsConfig
from materials.views import (MaterialsListView, MaterialsDetailView, MaterialsCreateView,
                             MaterialsUpdateView, MaterialsDeleteView)

app_name = MaterialsConfig.name

urlpatterns = [
    # path("materials/<int:pk>", MaterialsListView.as_view(), name="materials_list"),
    # path("materials/<int:pk>", MaterialsDetailView.as_view(), name="materials_detail"),
    path("materials/create", MaterialsCreateView.as_view(), name="create"),
    # path("materials/<int:pk>/update", MaterialsUpdateView.as_view(), name="materials_update"),
    # path("materials/<int:pk>/delete", MaterialsDeleteView.as_view(), name="materials_delete"),
]
