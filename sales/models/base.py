import uuid
from django.db import models


class BaseModel(models.Model):
    Id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_column="Id"
    )
    CreatedAt = models.DateTimeField(auto_now_add=True, db_column="CreatedAt")

    class Meta:
        abstract = True
