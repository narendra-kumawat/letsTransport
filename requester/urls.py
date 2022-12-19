from django.conf.urls import url
from requester.views import TransportAssetAPIView

urlpatterns = [
    url(r"^transport-asset/$", TransportAssetAPIView.as_view()),
]