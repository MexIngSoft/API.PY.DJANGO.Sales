from django.db import models
from .base import BaseModel


class Order(BaseModel):
    CustomerId = models.UUIDField(null=True, blank=True, db_column="IdCustomer")
    SalesChannel = models.CharField(max_length=100, db_column="SalesChannel")
    Status = models.CharField(max_length=50, db_column="Status")
    Total = models.DecimalField(
        max_digits=14, decimal_places=2, db_column="Total")

    class Meta:
        db_table = '"Sales"."Orders"'
