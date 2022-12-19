from core.models import BaseModel

from django.db import models


class RideInfo(BaseModel):
    source = models.CharField(max_length=500, verbose_name="Asset to be Picked From")
    destination = models.CharField(max_length=500, verbose_name="Asset Delivered to")
    datetime = models.DateTimeField()
