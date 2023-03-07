from django_filters.rest_framework import FilterSet
from .models import Student



class StudentFilter(FilterSet):
    class Meta:
        model = Student
        fields = {
            'department':['exact'],
            'gender':['exact'], 
            # 'status':['exact'],
            'semester':['exact'],
            'school':['exact'],

        }
              