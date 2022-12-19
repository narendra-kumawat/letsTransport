from core.views import BaseAPIView
from rider.models import TravelInfo
from rider.serializers import TravelInfoSerializer
from rider.filters import TravelInfoFilter


class TravelInfoAPIView(BaseAPIView):
    model_class = TravelInfo
    serializer_class = TravelInfoSerializer
    queryset = TravelInfo.objects.all()
    filter_class = TravelInfoFilter
