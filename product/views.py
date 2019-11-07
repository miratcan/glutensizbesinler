from django.views import generic
from . import models
from . import forms


class SupplierListView(generic.ListView):
    model = models.Supplier
    form_class = forms.SupplierForm


class SupplierDetailView(generic.DetailView):
    model = models.Supplier
    form_class = forms.SupplierForm


class BrandListView(generic.ListView):
    model = models.Brand
    form_class = forms.BrandForm


class BrandDetailView(generic.DetailView):
    model = models.Brand
    form_class = forms.BrandForm


class ProductListView(generic.ListView):
    model = models.Product
    form_class = forms.ProductForm


class ProductDetailView(generic.DetailView):
    model = models.Product
    form_class = forms.ProductForm


class SupplierTypeListView(generic.ListView):
    model = models.SupplierType
    form_class = forms.SupplierTypeForm


class SupplierTypeDetailView(generic.DetailView):
    model = models.SupplierType
    form_class = forms.SupplierTypeForm


class EvidenceListView(generic.ListView):
    model = models.Evidence
    form_class = forms.EvidenceForm


class EvidenceDetailView(generic.DetailView):
    model = models.Evidence
    form_class = forms.EvidenceForm

