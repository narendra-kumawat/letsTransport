from django_filters import CharFilter, FilterSet
from rider.models import TravelInfo


class TravelInfoFilter(FilterSet):
    matched_rides_only = CharFilter(method="get_matched_rides")

    def get_matched_rides(self, qs, field_name, value):
        if value not in [1, "true", "True"]:
            return qs

        return qs.filter(ride_info__transportationrequest__isnull=False).distinct()

    class Meta:
        model = TravelInfo
        fields = ("matched_rides_only",)