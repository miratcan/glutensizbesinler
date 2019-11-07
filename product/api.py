from rest_framework import viewsets, permissions

from . import serializers
from . import models


class NameAndSlugViewSet(viewsets.ModelViewSet):
    """ViewSet for the NameAndSlug class"""

    queryset = models.NameAndSlug.objects.all()
    serializer_class = serializers.NameAndSlugSerializer
    permission_classes = [permissions.IsAuthenticated]


class BaseModelViewSet(viewsets.ModelViewSet):
    """ViewSet for the BaseModel class"""

    queryset = models.BaseModel.objects.all()
    serializer_class = serializers.BaseModelSerializer
    permission_classes = [permissions.IsAuthenticated]


class SupplierViewSet(viewsets.ModelViewSet):
    """ViewSet for the Supplier class"""

    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer
    permission_classes = [permissions.IsAuthenticated]


class BrandViewSet(viewsets.ModelViewSet):
    """ViewSet for the Brand class"""

    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet for the Product class"""

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class SupplierTypeViewSet(viewsets.ModelViewSet):
    """ViewSet for the SupplierType class"""

    queryset = models.SupplierType.objects.all()
    serializer_class = serializers.SupplierTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class EvidenceViewSet(viewsets.ModelViewSet):
    """ViewSet for the Evidence class"""

    queryset = models.Evidence.objects.all()
    serializer_class = serializers.EvidenceSerializer
    permission_classes = [permissions.IsAuthenticated]
