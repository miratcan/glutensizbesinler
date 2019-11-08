from django.db import models
from django.urls import reverse

GLUTEN_STATUSES = (
    (None, 'Bilinmiyor'),
    (True, 'Var'),
    (False, 'Yok'),
)


class NameAndSlug(models.Model):

    #  Fields
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.name)


class BaseModel(models.Model):

    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True


class SupplierType(BaseModel, NameAndSlug):

    def get_absolute_url(self):
        return reverse("supplier_type_detail", args=(self.pk,))


class Supplier(BaseModel, NameAndSlug):

    #  Relationships
    type = models.ForeignKey(SupplierType, on_delete=models.CASCADE)

    #  Fields
    description = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    google_place_id = models.CharField(max_length=64, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("supplier_detail", args=(self.pk,))


class Brand(BaseModel, NameAndSlug):

    def get_absolute_url(self):
        return reverse("brand_detail", args=(self.pk,))


class Product(BaseModel, NameAndSlug):

    #  Relationships
    suppliers = models.ManyToManyField(Supplier, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    #  Fields
    gluten_status = models.NullBooleanField(choices=GLUTEN_STATUSES)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("product_detail", args=(self.pk,))


class Evidence(BaseModel):

    #  Relationships
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    #  Fields
    photo = models.ImageField(upload_to="upload/images/evidences/")
    note = models.TextField(null=True, blank=True)
    gluten_status = models.NullBooleanField(choices=GLUTEN_STATUSES)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("evidence_detail", args=(self.pk,))
