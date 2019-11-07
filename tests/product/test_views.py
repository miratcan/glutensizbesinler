import pytest
import test_helpers
from django.test import Client
from django.urls import reverse

pytestmark = [pytest.mark.django_db]


def tests_Supplier_list_view():
    instance1 = test_helpers.create_product_Supplier()
    instance2 = test_helpers.create_product_Supplier()
    client = Client()
    url = reverse("supplier_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Supplier_create_view():
    type = test_helpers.create_product_SupplierType()
    client = Client()
    url = reverse("product_Supplier_create")
    data = {
        "phone_number": "text",
        "google_place_id": "text",
        "address": "text",
        "type": type.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Supplier_detail_view():
    client = Client()
    instance = test_helpers.create_product_Supplier()
    url = reverse("product_Supplier_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Supplier_update_view():
    type = test_helpers.create_product_SupplierType()
    client = Client()
    instance = test_helpers.create_product_Supplier()
    url = reverse("product_Supplier_update", args=[instance.pk, ])
    data = {
        "phone_number": "text",
        "google_place_id": "text",
        "address": "text",
        "type": type.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Brand_list_view():
    instance1 = test_helpers.create_product_Brand()
    instance2 = test_helpers.create_product_Brand()
    client = Client()
    url = reverse("product_Brand_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Brand_create_view():
    client = Client()
    url = reverse("product_Brand_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Brand_detail_view():
    client = Client()
    instance = test_helpers.create_product_Brand()
    url = reverse("product_Brand_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Brand_update_view():
    client = Client()
    instance = test_helpers.create_product_Brand()
    url = reverse("product_Brand_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Product_list_view():
    instance1 = test_helpers.create_product_Product()
    instance2 = test_helpers.create_product_Product()
    client = Client()
    url = reverse("product_Product_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Product_create_view():
    supplier = test_helpers.create_product_Supplier()
    brand = test_helpers.create_product_Brand()
    client = Client()
    url = reverse("product_Product_create")
    data = {
        "gluten_status": true,
        "supplier": supplier.pk,
        "brand": brand.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Product_detail_view():
    client = Client()
    instance = test_helpers.create_product_Product()
    url = reverse("product_Product_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Product_update_view():
    supplier = test_helpers.create_product_Supplier()
    brand = test_helpers.create_product_Brand()
    client = Client()
    instance = test_helpers.create_product_Product()
    url = reverse("product_Product_update", args=[instance.pk, ])
    data = {
        "gluten_status": true,
        "supplier": supplier.pk,
        "brand": brand.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_SupplierType_list_view():
    instance1 = test_helpers.create_product_SupplierType()
    instance2 = test_helpers.create_product_SupplierType()
    client = Client()
    url = reverse("product_SupplierType_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_SupplierType_create_view():
    client = Client()
    url = reverse("product_SupplierType_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_SupplierType_detail_view():
    client = Client()
    instance = test_helpers.create_product_SupplierType()
    url = reverse("product_SupplierType_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_SupplierType_update_view():
    client = Client()
    instance = test_helpers.create_product_SupplierType()
    url = reverse("product_SupplierType_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Evidence_list_view():
    instance1 = test_helpers.create_product_Evidence()
    instance2 = test_helpers.create_product_Evidence()
    client = Client()
    url = reverse("product_Evidence_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Evidence_create_view():
    author = test_helpers.create_User()
    client = Client()
    url = reverse("product_Evidence_create")
    data = {
        "photo": "anImage",
        "note": "text",
        "gluten_status": true,
        "author": author.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Evidence_detail_view():
    client = Client()
    instance = test_helpers.create_product_Evidence()
    url = reverse("product_Evidence_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Evidence_update_view():
    author = test_helpers.create_User()
    client = Client()
    instance = test_helpers.create_product_Evidence()
    url = reverse("product_Evidence_update", args=[instance.pk, ])
    data = {
        "photo": "anImage",
        "note": "text",
        "gluten_status": true,
        "author": author.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
