from django.contrib import admin
from django import forms

from . import models


class SupplierAdminForm(forms.ModelForm):

    class Meta:
        model = models.Supplier
        fields = "__all__"


class SupplierAdmin(admin.ModelAdmin):
    form = SupplierAdminForm
    list_display = [
        "name",
        "phone_number",
        "google_place_id",
        "address",
    ]


class BrandAdminForm(forms.ModelForm):

    class Meta:
        model = models.Brand
        fields = "__all__"


class BrandAdmin(admin.ModelAdmin):
    form = BrandAdminForm
    list_display = [
        "name"
    ]
    readonly_fields = [
    ]


class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = "__all__"


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = [
        "name",
        "brand",
        "gluten_status",
    ]
    readonly_fields = [
        "gluten_status",
    ]


class SupplierTypeAdminForm(forms.ModelForm):

    class Meta:
        model = models.SupplierType
        fields = "__all__"


class SupplierTypeAdmin(admin.ModelAdmin):
    form = SupplierTypeAdminForm
    readonly_fields = [
    ]


class EvidenceAdminForm(forms.ModelForm):

    class Meta:
        model = models.Evidence
        fields = "__all__"


class EvidenceAdmin(admin.ModelAdmin):
    form = EvidenceAdminForm
    list_display = [
        "photo",
        "note",
        "gluten_status",
    ]
    readonly_fields = [
        "photo",
        "note",
        "gluten_status",
    ]


admin.site.register(models.Supplier, SupplierAdmin)
admin.site.register(models.Brand, BrandAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.SupplierType, SupplierTypeAdmin)
admin.site.register(models.Evidence, EvidenceAdmin)
