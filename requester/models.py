from django.db import models

from core.models import BaseModel
from util.models import RideInfo


class AssetSensitivity:
    HIGHLY_SENSITIVE = "highly_sensitive"
    SENSITIVE = "sensitive"
    NORMAL = "high"


class AssetChoices:
    CONFIRM = "confirm"
    PENDING = "pending"
    EXPIRED = "expired"


class AssetType:
    LAPTOP = "laptop"
    TRAVEL_BAG = "travel_bag"
    PACKAGE = "package"


class AssetStatus:
    CONFIRM = "confirm"
    PENDING = "pending"
    EXPIRED = "expired"


class TransportationRequest(BaseModel):
    ASSET_SENSITIVITY_CHOICES = (
        (AssetSensitivity.HIGHLY_SENSITIVE, AssetSensitivity.HIGHLY_SENSITIVE),
        (AssetSensitivity.SENSITIVE, AssetSensitivity.SENSITIVE),
        (AssetSensitivity.NORMAL, AssetSensitivity.NORMAL),
    )
    ASSET_STATUS_CHOICES = (
        (AssetChoices.CONFIRM, AssetChoices.CONFIRM),
        (AssetChoices.PENDING, AssetChoices.PENDING),
        (AssetChoices.EXPIRED, AssetChoices.EXPIRED),
    )
    ASSET_TYPE_CHOICES = (
        (AssetType.LAPTOP, AssetType.LAPTOP),
        (AssetType.PACKAGE, AssetType.PACKAGE),
        (AssetType.TRAVEL_BAG, AssetType.TRAVEL_BAG),
    )
    ride_info = models.ForeignKey(RideInfo, on_delete=models.CASCADE)
    no_of_assets = models.PositiveIntegerField()
    asset_type = models.CharField(max_length=30, choices=ASSET_TYPE_CHOICES)
    asset_sensitivity = models.CharField(
        max_length=30, choices=ASSET_SENSITIVITY_CHOICES
    )
    status = models.CharField(
        max_length=50, choices=ASSET_STATUS_CHOICES, default=AssetStatus.PENDING
    )
    whom_to_deliver = models.CharField(max_length=300)
