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
    path("suppliers/", views.SupplierListView.as_view(), name="supplier_list"),
    path("supplier/<int:pk>/",
        views.SupplierDetailView.as_view(), name="supplier_detail"),
    path("brands/", views.BrandListView.as_view(), name="brand_list"),
    path("brand/<int:pk>/", views.BrandDetailView.as_view(), name="brand_detail"),
    path("<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("supplier_types/", views.SupplierTypeListView.as_view(),
        name="supplier_type_list"),
    path("supplier_type/<int:pk>/", views.SupplierTypeDetailView.as_view(),
        name="supplier_type_detail"),
    path("evidences/", views.EvidenceListView.as_view(), name="evidence_list"),
    path("evidence/<int:pk>/", views.EvidenceDetailView.as_view(), name="evidence_detail"),
)
