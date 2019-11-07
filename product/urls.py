from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("NameAndSlug", api.NameAndSlugViewSet)
router.register("BaseModel", api.BaseModelViewSet)
router.register("Supplier", api.SupplierViewSet)
router.register("Brand", api.BrandViewSet)
router.register("Product", api.ProductViewSet)
router.register("SupplierType", api.SupplierTypeViewSet)
router.register("Evidence", api.EvidenceViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("product/NameAndSlug/", views.NameAndSlugListView.as_view(), name="product_NameAndSlug_list"),
    path("product/NameAndSlug/create/", views.NameAndSlugCreateView.as_view(), name="product_NameAndSlug_create"),
    path("product/NameAndSlug/detail/<slug:slug>/", views.NameAndSlugDetailView.as_view(), name="product_NameAndSlug_detail"),
    path("product/NameAndSlug/update/<slug:slug>/", views.NameAndSlugUpdateView.as_view(), name="product_NameAndSlug_update"),
    path("product/BaseModel/", views.BaseModelListView.as_view(), name="product_BaseModel_list"),
    path("product/BaseModel/create/", views.BaseModelCreateView.as_view(), name="product_BaseModel_create"),
    path("product/BaseModel/detail/<int:pk>/", views.BaseModelDetailView.as_view(), name="product_BaseModel_detail"),
    path("product/BaseModel/update/<int:pk>/", views.BaseModelUpdateView.as_view(), name="product_BaseModel_update"),
    path("product/Supplier/", views.SupplierListView.as_view(), name="product_Supplier_list"),
    path("product/Supplier/create/", views.SupplierCreateView.as_view(), name="product_Supplier_create"),
    path("product/Supplier/detail/<int:pk>/", views.SupplierDetailView.as_view(), name="product_Supplier_detail"),
    path("product/Supplier/update/<int:pk>/", views.SupplierUpdateView.as_view(), name="product_Supplier_update"),
    path("product/Brand/", views.BrandListView.as_view(), name="product_Brand_list"),
    path("product/Brand/create/", views.BrandCreateView.as_view(), name="product_Brand_create"),
    path("product/Brand/detail/<int:pk>/", views.BrandDetailView.as_view(), name="product_Brand_detail"),
    path("product/Brand/update/<int:pk>/", views.BrandUpdateView.as_view(), name="product_Brand_update"),
    path("product/Product/", views.ProductListView.as_view(), name="product_Product_list"),
    path("product/Product/create/", views.ProductCreateView.as_view(), name="product_Product_create"),
    path("product/Product/detail/<int:pk>/", views.ProductDetailView.as_view(), name="product_Product_detail"),
    path("product/Product/update/<int:pk>/", views.ProductUpdateView.as_view(), name="product_Product_update"),
    path("product/SupplierType/", views.SupplierTypeListView.as_view(), name="product_SupplierType_list"),
    path("product/SupplierType/create/", views.SupplierTypeCreateView.as_view(), name="product_SupplierType_create"),
    path("product/SupplierType/detail/<int:pk>/", views.SupplierTypeDetailView.as_view(), name="product_SupplierType_detail"),
    path("product/SupplierType/update/<int:pk>/", views.SupplierTypeUpdateView.as_view(), name="product_SupplierType_update"),
    path("product/Evidence/", views.EvidenceListView.as_view(), name="product_Evidence_list"),
    path("product/Evidence/create/", views.EvidenceCreateView.as_view(), name="product_Evidence_create"),
    path("product/Evidence/detail/<int:pk>/", views.EvidenceDetailView.as_view(), name="product_Evidence_detail"),
    path("product/Evidence/update/<int:pk>/", views.EvidenceUpdateView.as_view(), name="product_Evidence_update"),
)
