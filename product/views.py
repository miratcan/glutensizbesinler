
from django.views import generic
from search_views.filters import BaseFilter
from search_views.search import SearchListView

from . import models
from .forms import ProductSearchForm


class ProductFilter(BaseFilter):
    search_fields = {
        'q' : ['name', ],
    }


class SupplierListView(generic.ListView):
    model = models.Supplier


class SupplierDetailView(generic.DetailView):
    model = models.Supplier


class BrandListView(generic.ListView):
    model = models.Brand


class BrandDetailView(generic.DetailView):
    model = models.Brand


class ProductListView(SearchListView):
    model = models.Product
    paginate_by = 20
    page_kwarg = 'p'
    form_class = ProductSearchForm
    filter_class = ProductFilter
    template_name = 'index.html'
    prefetch_fields = ['brand', ]

class ProductDetailView(generic.DetailView):
    model = models.Product


class SupplierTypeListView(generic.ListView):
    model = models.SupplierType


class SupplierTypeDetailView(generic.DetailView):
    model = models.SupplierType


class EvidenceListView(generic.ListView):
    model = models.Evidence


class EvidenceDetailView(generic.DetailView):
    model = models.Evidence
