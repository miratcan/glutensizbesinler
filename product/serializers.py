from rest_framework import serializers

from . import models


class NameAndSlugSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.NameAndSlug
        fields = [
            "slug",
            "name",
        ]

class BaseModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BaseModel
        fields = [
            "updated_at",
            "created_at",
        ]

class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Supplier
        fields = [
            "phone_number",
            "google_place_id",
            "address",
        ]

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Brand
        fields = [
        ]

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = [
            "gluten_status",
        ]

class SupplierTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SupplierType
        fields = [
        ]

class EvidenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Evidence
        fields = [
            "photo",
            "note",
            "gluten_status",
        ]
