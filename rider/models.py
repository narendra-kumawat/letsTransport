from django.db import models

from core.models import BaseModel
from util.models import RideInfo

from django.core.validators import MinValueValidator


class TravelMedium:
    BUS = "bus"
    CAR = "car"
    TRAIN = "train"


class TravelStatus:
    APPLIED = "applied"
    NOT_APPLIED = "not_applied"


class TravelInfo(BaseModel):
    TRAVEL_MEDIUM_CHOICES = (
        (TravelMedium.BUS, TravelMedium.BUS),
        (TravelMedium.CAR, TravelMedium.CAR),
        (TravelMedium.TRAIN, TravelMedium.TRAIN),
    )

    TRAVEL_STATUS_CHOICES = (
        (TravelStatus.APPLIED, TravelStatus.APPLIED),
        (TravelStatus.NOT_APPLIED, TravelStatus.NOT_APPLIED),
    )
    ride_info = models.ForeignKey(RideInfo, on_delete=models.CASCADE)
    no_of_assets = models.PositiveIntegerField(validators=[MinValueValidator(limit_value=1)])
    travel_medium = models.CharField(max_length=30, choices=TRAVEL_MEDIUM_CHOICES)
    status = models.CharField(max_length=30, default=TravelStatus.NOT_APPLIED, choices=TRAVEL_STATUS_CHOICES)
    ride_accepted_by = models.CharField(
        max_length=300,
        null=True,
        default=None,
        verbose_name="Ride accepted by the Person's Detail",
    )
