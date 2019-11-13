from django.db import models
from django.urls import reverse
from django_mysql.models import JSONField, Model

GLUTEN_STATUSES = (
    (0, 'Yok'),
    (1, 'Büyük İhtimalle Yok'),
    (2, 'Belirsiz'),
    (3, 'Küçük İhtimalle Var'),
    (3, 'Büyük İhtimalle Var'),
)


class NameAndSlug(Model):
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
    def get_absolute_url(self):
        return reverse("supplier_type_detail", args=(self.pk,))


class Supplier(BaseModel, NameAndSlug):
    type = models.ForeignKey(SupplierType, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse("supplier_detail", args=(self.pk,))


class Brand(BaseModel, NameAndSlug):
    def get_absolute_url(self):
        return reverse("brand_detail", args=(self.pk,))


class Product(BaseModel, NameAndSlug):
    photo = models.ImageField(upload_to='products/')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    evidences = models.ManyToManyField('product.Evidence', blank=True)
    gluten_status = models.PositiveSmallIntegerField(choices=GLUTEN_STATUSES)

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
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="upload/images/evidences/")
    note = models.TextField(null=True, blank=True)
    gluten_status = models.PositiveSmallIntegerField(choices=GLUTEN_STATUSES)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("evidence_detail", args=(self.pk,))
