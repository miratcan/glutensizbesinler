from django import forms
from django.contrib import admin

from . import models


class NameAndSlugMixin(object):
    prepopulated_fields = {"slug": ("name",)}


class SupplierAdminForm(forms.ModelForm):
    # TODO
    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get("data")
        subject = cleaned_data.get("subject")

        if cc_myself and subject:
            # Only do something if both fields are valid so far.
            if "help" not in subject:
                raise forms.ValidationError(
                    "Did not send for 'help' in the subject despite "
                    "CC'ing yourself."
                )

    class Meta:
        model = models.Supplier
        fields = "__all__"


class SupplierAdmin(NameAndSlugMixin, admin.ModelAdmin):
    form = SupplierAdminForm
    list_display = ["name",]


class BrandAdminForm(forms.ModelForm):

    class Meta:
        model = models.Brand
        fields = "__all__"


class BrandAdmin(NameAndSlugMixin, admin.ModelAdmin):
    form = BrandAdminForm
    list_display = ["name"]


class ObtainMethodInline(admin.TabularInline):
    model = models.ObtainMethod


class ProductAdminForm(forms.ModelForm):
    
    class Meta:
        model = models.Product
        prepopulated_fields = {"slug": ("name",)}
        fields = "__all__"



class ProductAdmin(NameAndSlugMixin, admin.ModelAdmin):
    form = ProductAdminForm
    inlines = (ObtainMethodInline,)
    list_display = [
        "name",
        "brand",
        "gluten_status",
    ]
    readonly_fields = [
        "gluten_status",
    ]
    filter_horizontal = [
        "evidences"
    ]


class SupplierTypeAdminForm(forms.ModelForm):

    class Meta:
        model = models.SupplierType
        fields = "__all__"


class SupplierTypeAdmin(NameAndSlugMixin, admin.ModelAdmin):
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


admin.site.register(models.Supplier, SupplierAdmin)
admin.site.register(models.Brand, BrandAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.SupplierType, SupplierTypeAdmin)
admin.site.register(models.Evidence, EvidenceAdmin)
