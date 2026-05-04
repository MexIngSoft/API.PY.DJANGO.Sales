from django.db import models
from .base import BaseModel
from .quote import Quote


class QuoteItem(BaseModel):
    Quote = models.ForeignKey(
        Quote, on_delete=models.CASCADE, related_name="Items", db_column="IdQuote")
    ProductId = models.UUIDField(db_column="IdProduct")
    Quantity = models.IntegerField(db_column="Quantity")
    UnitPrice = models.DecimalField(
        max_digits=18, decimal_places=6, db_column="UnitPrice")
    SupplierAvailableQty = models.IntegerField(
        default=0, db_column="SupplierAvailableQty")
    LocalAvailableQty = models.IntegerField(
        default=0, db_column="LocalAvailableQty")
    AvailabilityCapturedAt = models.DateTimeField(
        null=True, blank=True, db_column="AvailabilityCapturedAt")
    DeliveryMode = models.CharField(max_length=50, db_column="DeliveryMode")

    class Meta:
        db_table = '"Sales"."QuoteItems"'
        indexes = [
            models.Index(fields=["Quote"], name="IX_QuoteItems_Quote"),
            models.Index(fields=["ProductId"], name="IX_QuoteItems_Product"),
        ]
