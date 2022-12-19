from core.serializers import BaseModelSerializer
from util.models import RideInfo


class RideInfoSerializer(BaseModelSerializer):
    class Meta:
        model = RideInfo
        fields = ("source", "destination", "datetime")
