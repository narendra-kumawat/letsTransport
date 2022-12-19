from core.views import BaseAPIView
from requester.models import TransportationRequest, AssetStatus
from requester.serializers import TransportationRequestSerializer
from requester.filters import TransportationRequestFilter
from django.utils import timezone


class TransportAssetAPIView(BaseAPIView):
    model_class = TransportationRequest
    serializer_class = TransportationRequestSerializer
    queryset = model_class.objects.all()
    ordering_fields = ("ride_info__datetime",)
    filter_class = TransportationRequestFilter

    def get_queryset(self):
        now = timezone.now()
        expired_requests = self.queryset.filter(ride_info__datetime__lt=now)
        expired_requests.update(status=AssetStatus)
        return self.model_class.objects.all()
