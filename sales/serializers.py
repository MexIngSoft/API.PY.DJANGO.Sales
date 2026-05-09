from datetime import timedelta

from django.utils import timezone
from rest_framework import serializers

from .models import Quote, QuoteItem


class QuoteItemSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="Id", read_only=True)
    productId = serializers.UUIDField(source="ProductId")
    quantity = serializers.IntegerField(source="Quantity", min_value=1)
    unitPrice = serializers.DecimalField(source="UnitPrice", max_digits=18, decimal_places=6)
    supplierAvailableQty = serializers.IntegerField(source="SupplierAvailableQty", required=False, default=0)
    localAvailableQty = serializers.IntegerField(source="LocalAvailableQty", required=False, default=0)
    deliveryMode = serializers.CharField(source="DeliveryMode", required=False, default="TO_CONFIRM")

    class Meta:
        model = QuoteItem
        fields = [
            "id",
            "productId",
            "quantity",
            "unitPrice",
            "supplierAvailableQty",
            "localAvailableQty",
            "deliveryMode",
        ]


class QuoteSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="Id", read_only=True)
    customerId = serializers.UUIDField(source="CustomerId", required=False, allow_null=True)
    status = serializers.CharField(source="Status", required=False)
    validUntil = serializers.DateTimeField(source="ValidUntil", required=False)
    notes = serializers.CharField(source="Notes", required=False, allow_blank=True, allow_null=True)
    items = QuoteItemSerializer(source="Items", many=True, required=False)

    class Meta:
        model = Quote
        fields = ["id", "customerId", "status", "validUntil", "notes", "items"]

    def create(self, validated_data):
        items = validated_data.pop("Items", [])
        validated_data.setdefault("Status", "NEW")
        validated_data.setdefault("ValidUntil", timezone.now() + timedelta(days=15))
        quote = Quote.objects.create(**validated_data)
        for item in items:
            QuoteItem.objects.create(Quote=quote, **item)
        return quote
