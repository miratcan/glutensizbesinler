import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from product import models as product_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_product_Supplier(**kwargs):
    defaults = {}
    defaults["phone_number"] = ""
    defaults["google_place_id"] = ""
    defaults["address"] = ""
    defaults["updated_at"] = datetime.now()
    defaults["created_at"] = datetime.now()
    defaults["slug"] = "slug"
    defaults["name"] = "text"
    if "type" not in kwargs:
        defaults["type"] = create_product_SupplierType()
    defaults.update(**kwargs)
    return product_models.Supplier.objects.create(**defaults)
def create_product_Brand(**kwargs):
    defaults = {}
    defaults["updated_at"] = datetime.now()
    defaults["created_at"] = datetime.now()
    defaults["slug"] = "slug"
    defaults["name"] = "text"
    defaults.update(**kwargs)
    return product_models.Brand.objects.create(**defaults)
def create_product_Product(**kwargs):
    defaults = {}
    defaults["gluten_status"] = ""
    defaults["updated_at"] = datetime.now()
    defaults["created_at"] = datetime.now()
    defaults["slug"] = "slug"
    defaults["name"] = "text"
    if "supplier" not in kwargs:
        defaults["supplier"] = create_product_Supplier()
    if "brand" not in kwargs:
        defaults["brand"] = create_product_Brand()
    defaults.update(**kwargs)
    return product_models.Product.objects.create(**defaults)
def create_product_SupplierType(**kwargs):
    defaults = {}
    defaults["updated_at"] = datetime.now()
    defaults["created_at"] = datetime.now()
    defaults["slug"] = "slug"
    defaults["name"] = "text"
    defaults.update(**kwargs)
    return product_models.SupplierType.objects.create(**defaults)
def create_product_Evidence(**kwargs):
    defaults = {}
    defaults["photo"] = ""
    defaults["note"] = ""
    defaults["gluten_status"] = ""
    defaults["updated_at"] = datetime.now()
    defaults["created_at"] = datetime.now()
    if "author" not in kwargs:
        defaults["author"] = create_User()
    defaults.update(**kwargs)
    return product_models.Evidence.objects.create(**defaults)
