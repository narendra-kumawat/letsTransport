from django_filters import CharFilter, FilterSet
from requester.models import TransportationRequest


class TransportationRequestFilter(FilterSet):
    class Meta:
        model = TransportationRequest
        fields = ("status", "asset_type")
