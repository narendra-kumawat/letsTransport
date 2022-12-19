from core.serializers import BaseModelSerializer
from rider.models import TravelInfo
from util.models import RideInfo
from util.serializers import RideInfoSerializer
from rest_framework import serializers


class TravelInfoSerializer(BaseModelSerializer):
    ride_info = RideInfoSerializer(read_only=True)
    source = serializers.CharField(write_only=True)
    destination = serializers.CharField(write_only=True)
    datetime = serializers.DateTimeField(write_only=True)

    def save(self, **kwargs):
        if not self.instance:
            ride_info, created = RideInfo.objects.get_or_create(
                source=self.validated_data.pop("source"),
                destination=self.validated_data.pop("destination"),
                datetime=self.validated_data.pop("datetime"),
            )
            self.validated_data["ride_info"] = ride_info

        return super().save(**kwargs)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        ride_info = data.pop("ride_info")
        data.update(ride_info)
        return data

    class Meta:
        model = TravelInfo
        fields = (
            "source",
            "destination",
            "datetime",
            "no_of_assets",
            "travel_medium",
            "status",
            "ride_accepted_by",
            "ride_info"
        )
