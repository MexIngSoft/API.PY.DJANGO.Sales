from django.db import models
from .base import BaseModel


class Quote(BaseModel):
    CustomerId = models.UUIDField(null=True, blank=True, db_column="IdCustomer")
    Status = models.CharField(max_length=30, default="DRAFT", db_column="Status")
    ValidUntil = models.DateTimeField(db_column="ValidUntil")
    Notes = models.TextField(null=True, blank=True, db_column="Notes")

    class Meta:
        db_table = '"Sales"."Quotes"'
        indexes = [
            models.Index(fields=["CustomerId", "Status"], name="IX_Quotes_Customer_Status"),
            models.Index(fields=["ValidUntil"], name="IX_Quotes_ValidUntil"),
        ]
