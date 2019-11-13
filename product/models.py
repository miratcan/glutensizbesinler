from django.db import models
from django.urls import reverse
from django_mysql.models import JSONField, Model

GLUTEN_STATUSES = (
    (None, 'Bilinmiyor'),
    (True, 'Var'),
    (False, 'Yok'),
)


class NameAndSlug(Model):

    #  Fields
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.name)


class BaseModel(Model):

    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True


class SupplierType(BaseModel, NameAndSlug):
    fields = JSONField(default=list)
    def get_absolute_url(self):
        return reverse("supplier_type_detail", args=(self.pk,))


class Supplier(BaseModel, NameAndSlug):

    #  Relationships
    type = models.ForeignKey(SupplierType, on_delete=models.CASCADE)
    data = JSONField(null=True, blank=True, default=dict)

    def get_absolute_url(self):
        return reverse("supplier_detail", args=(self.pk,))


class Brand(BaseModel, NameAndSlug):

    def get_absolute_url(self):
        return reverse("brand_detail", args=(self.pk,))




class Product(BaseModel, NameAndSlug):

    #  Relationships
    suppliers = models.ManyToManyField(Supplier)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    evidences = models.ManyToManyField('product.Evidence', blank=True)

    #  Fields
    gluten_status = models.NullBooleanField(choices=GLUTEN_STATUSES)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("product_detail", args=(self.pk,))


class ObtainMethod(Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="obtain_methods")
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    data = JSONField(null=True, blank=True, default=dict)


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
