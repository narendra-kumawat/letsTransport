from django.conf.urls import url
from rider.views import TravelInfoAPIView

urlpatterns = [
    url(r"^travel-info/$", TravelInfoAPIView.as_view()),
    url(r"^travel-info/(?P<id>[\w\d-]+)/$", TravelInfoAPIView.as_view()),
]