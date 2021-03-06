from django.urls import include, path
from rest_framework import routers

from . import api, views

router = routers.DefaultRouter()
router.register("Supplier", api.SupplierViewSet)
router.register("Brand", api.BrandViewSet)
router.register("Product", api.ProductViewSet)
router.register("SupplierType", api.SupplierTypeViewSet)
router.register("Evidence", api.EvidenceViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("tedarikci/<int:pk>/",
        views.SupplierDetailView.as_view(), name="supplier_detail"),
    path("markalar/", views.BrandListView.as_view(), name="brand_list"),
    path("marka/<int:pk>/", views.BrandDetailView.as_view(), name="brand_detail"),
    path("<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("tedarikci_tipleri/", views.SupplierTypeListView.as_view(),
        name="supplier_type_list"),
    path("tedarikci_tipi/<int:pk>/", views.SupplierTypeDetailView.as_view(),
        name="supplier_type_detail"),
    path("kanitlar/", views.EvidenceListView.as_view(), name="evidence_list"),
    path("kanit/<int:pk>/", views.EvidenceDetailView.as_view(), name="evidence_detail"),
)
