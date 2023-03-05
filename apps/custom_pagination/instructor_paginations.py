from rest_framework.pagination import PageNumberPagination

class InstructorPaginator(PageNumberPagination):
    page_size = 1