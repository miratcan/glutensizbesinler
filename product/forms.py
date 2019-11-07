from django import forms
from . import models


class SupplierForm(forms.ModelForm):
    class Meta:
        model = models.Supplier
        fields = [
            "phone_number",
            "google_place_id",
            "address",
            "type",
        ]


class BrandForm(forms.ModelForm):
    class Meta:
        model = models.Brand
        fields = []



class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = [
            "gluten_status",
            "supplier",
            "brand",
        ]


class SupplierTypeForm(forms.ModelForm):
    class Meta:
        model = models.SupplierType
        fields = []



class EvidenceForm(forms.ModelForm):
    class Meta:
        model = models.Evidence
        fields = [
            "photo",
            "note",
            "gluten_status",
            "author",
        ]
