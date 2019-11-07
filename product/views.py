from django.views import generic
from . import models
from . import forms


class SupplierListView(generic.ListView):
    model = models.Supplier
    form_class = forms.SupplierForm


class SupplierCreateView(generic.CreateView):
    model = models.Supplier
    form_class = forms.SupplierForm


class SupplierDetailView(generic.DetailView):
    model = models.Supplier
    form_class = forms.SupplierForm


class SupplierUpdateView(generic.UpdateView):
    model = models.Supplier
    form_class = forms.SupplierForm
    pk_url_kwarg = "pk"


class BrandListView(generic.ListView):
    model = models.Brand
    form_class = forms.BrandForm


class BrandCreateView(generic.CreateView):
    model = models.Brand
    form_class = forms.BrandForm


class BrandDetailView(generic.DetailView):
    model = models.Brand
    form_class = forms.BrandForm


class BrandUpdateView(generic.UpdateView):
    model = models.Brand
    form_class = forms.BrandForm
    pk_url_kwarg = "pk"


class ProductListView(generic.ListView):
    model = models.Product
    form_class = forms.ProductForm


class ProductCreateView(generic.CreateView):
    model = models.Product
    form_class = forms.ProductForm


class ProductDetailView(generic.DetailView):
    model = models.Product
    form_class = forms.ProductForm


class ProductUpdateView(generic.UpdateView):
    model = models.Product
    form_class = forms.ProductForm
    pk_url_kwarg = "pk"


class SupplierTypeListView(generic.ListView):
    model = models.SupplierType
    form_class = forms.SupplierTypeForm


class SupplierTypeCreateView(generic.CreateView):
    model = models.SupplierType
    form_class = forms.SupplierTypeForm


class SupplierTypeDetailView(generic.DetailView):
    model = models.SupplierType
    form_class = forms.SupplierTypeForm


class SupplierTypeUpdateView(generic.UpdateView):
    model = models.SupplierType
    form_class = forms.SupplierTypeForm
    pk_url_kwarg = "pk"


class EvidenceListView(generic.ListView):
    model = models.Evidence
    form_class = forms.EvidenceForm


class EvidenceCreateView(generic.CreateView):
    model = models.Evidence
    form_class = forms.EvidenceForm


class EvidenceDetailView(generic.DetailView):
    model = models.Evidence
    form_class = forms.EvidenceForm


class EvidenceUpdateView(generic.UpdateView):
    model = models.Evidence
    form_class = forms.EvidenceForm
    pk_url_kwarg = "pk"
