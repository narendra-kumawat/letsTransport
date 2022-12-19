from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils.functional import cached_property


class CustomPaginator(Paginator):
    @cached_property
    def count(self):
        """Return the total number of objects, across all pages."""
        try:
            return self.object_list.only("pk").count()
        except (AttributeError, TypeError):
            # AttributeError if object_list has no count() method.
            # TypeError if object_list.count() requires arguments
            # (i.e. is of type list).
            return len(self.object_list)


class PaginationMixin(object):
    """ Pagination mixin to paginate list of objects"""

    PAGE_SIZE = 10

    def _get_page_link(self, base_path, query_params, page_num, page_size):
        """ Appends query params to the base path for page_num and page_size"""
        query_params_dict = query_params.dict()
        query_params_dict.pop("page", None)
        query_params_dict.pop("page_size", None)

        link = "{path}?page={page_num}&page_size={page_size}".format(
            path=base_path, page_num=page_num, page_size=page_size
        )

        # Updating existing query params in url
        if query_params_dict:
            query_str = "&".join(
                [
                    "{0}={1}".format(key, value)
                    for key, value in query_params_dict.items()
                ]
            )
            link = "{0}&{1}".format(link, query_str)

        return link

    def paginate_data(self, request, object_queryset):
        """Given object queryset, returns paginated data.
        Returns dictionary with following keys:
        1. link: another dictionary providing links to next and previous pages if
        applicable
        2. count: Total number of objects across pages
        3. results: list of objects or list of serialized data depends if serializer
        is present or not.

        You should send unevaluated queryset as the paginator will use it to fetch only
        subset of data. If you are sending list, that pagination will work but you have
        already fetched whole data.

        """

        page_num = request.query_params.get("page", 1)
        page_size = request.query_params.get("page_size")
        base_path = request.path

        # Get all data in one page if requested all_data param is True
        if request.query_params.get("all_data", "false").lower() == "true":
            page_size = object_queryset.count()
            if page_size == 0:
                page_size = None

        paginated_data_dict = self.get_paginated_data(
            base_path, request.query_params, object_queryset, page_num, page_size
        )

        paginated_data = paginated_data_dict.get("results", [])
        processed_data = self.process_paginated_data(paginated_data)
        paginated_data_dict["results"] = processed_data

        return paginated_data_dict

    def process_paginated_data(self, paginated_data):
        """Post process subset of data to be sent as paginated response. In this the
        input is queryset of paginated data. This method takes this queryset and
        returns serialized data
        paginated_data: paginated data queryset
        """

        # Make sure you override get_serializer method or add serializer class on which
        #  the mixin will be applied
        fields = self.request.query_params.get("fields", "")
        fields = [field.strip() for field in fields.split(",") if field]
        fields = fields or None

        serialized_data = self.get_serializer(
            paginated_data, many=True,
            # fields=fields
        ).data
        return serialized_data

    def get_paginated_data(
        self, base_path, query_params, object_list, page_num=1, page_size=None
    ):
        if page_size is None:
            page_size = self.PAGE_SIZE
        paginator = CustomPaginator(object_list, page_size)

        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        page_object_list = page_obj.object_list

        next_page_link = None
        if page_obj.has_next():
            next_page_link = self._get_page_link(
                base_path, query_params, page_obj.next_page_number(), page_size
            )

        previous_page_link = None
        if page_obj.has_previous():
            previous_page_link = self._get_page_link(
                base_path, query_params, page_obj.previous_page_number(), page_size
            )

        link = {}
        if next_page_link:
            # Remove / from the end as frontend will be broken
            link["next"] = next_page_link.lstrip("/")
        if previous_page_link:
            link["previous"] = previous_page_link.lstrip("/")

        return {"link": link, "count": paginator.count, "results": page_object_list}
