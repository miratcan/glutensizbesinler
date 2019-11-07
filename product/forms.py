from django import forms

from . import models


class ProductSearchForm(forms.Form):
    q = forms.CharField(required=False)
