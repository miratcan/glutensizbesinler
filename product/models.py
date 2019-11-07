from django.db import models
from django.urls import reverse


class NameAndSlug(models.Model):

    #  Fields
    slug = models.SlugField(max_length=32)
    name = models.CharField(max_length=32)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("product_NameAndSlug_detail", args=(self.slug,))

    def get_update_url(self):
        return reverse("product_NameAndSlug_update", args=(self.slug,))


class BaseModel(models.Model):

    #  Fields
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("product_BaseModel_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("product_BaseModel_update", args=(self.pk,))


class Supplier(BaseModel, NameAndSlug):

    #  Relationships
    type = models.ForeignKey("undefined.SupplierType", on_delete=models.CASCADE)

    #  Fields
    phone_number = models.CharField(max_length=32)
    google_place_id = models.CharField(max_length=64)
    address = models.TextField(null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("product_Supplier_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("product_Supplier_update", args=(self.pk,))


class Brand(BaseModel, NameAndSlug):

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("product_Brand_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("product_Brand_update", args=(self.pk,))


class Product(BaseModel, NameAndSlug):

    #  Relationships
    supplier = models.ForeignKey("undefined.Supplier", on_delete=models.CASCADE)
    brand = models.ForeignKey("undefined.Brand", on_delete=models.CASCADE)

    #  Fields
    gluten_status = models.NullBooleanField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("product_Product_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("product_Product_update", args=(self.pk,))


class SupplierType(BaseModel, NameAndSlug):

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("product_SupplierType_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("product_SupplierType_update", args=(self.pk,))


class Evidence(BaseModel):

    #  Relationships
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    #  Fields
    photo = models.ImageField(upload_to="/upload/images/evidences/")
    note = models.TextField(null=True, blank=True)
    gluten_status = models.NullBooleanField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("product_Evidence_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("product_Evidence_update", args=(self.pk,))