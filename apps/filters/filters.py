from django_filters.rest_framework import FilterSet
from apps.custom_models.instructors_models import Staff



class StaffFilter(FilterSet):
    class Meta:
        model = Staff
        fields = {
            'department':['exact'],
            'gender':['exact'], 
            'status':['exact'],
        }
              