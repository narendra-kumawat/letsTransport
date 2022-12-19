from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from core.pagination_mixin import PaginationMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class BaseAPIView(GenericAPIView, PaginationMixin):
    authentication_classes = ()
    filter_backends = (DjangoFilterBackend, OrderingFilter)

    def get(self, request, id=None):
        if not id:
            return self.get_list(request)

        # Here specific object view can be implemented (in-case required)
        # As of now, just returning empty response.
        return Response()

    def get_list(self, request):
        qs = self.get_queryset()
        qs = self.filter_queryset(queryset=qs)
        self.paginate_data(request, qs)
        paginated_data_dict = self.paginate_data(request, qs)
        return Response(paginated_data_dict, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response({"id": instance.pk}, status=status.HTTP_200_OK)

    def put(self, request, id):
        instance = self.queryset.filter(id=id).first()
        if not instance:
            return Response({"Error": "Invalid ID"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(instance=instance, data=self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(status=status.HTTP_200_OK)
