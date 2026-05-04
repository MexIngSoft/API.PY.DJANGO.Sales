from django.db import models
from .base import BaseModel


class OrderItem(BaseModel):
    OrderId = models.UUIDField(db_column="IdOrder")
    ProductId = models.UUIDField(db_column="IdProduct")
    Quantity = models.IntegerField(db_column="Quantity")
    Price = models.DecimalField(
        max_digits=12, decimal_places=2, db_column="Price")

    class Meta:
        db_table = '"Sales"."OrderItems"'
