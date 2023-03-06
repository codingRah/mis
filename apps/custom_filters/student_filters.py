from django_filters.rest_framework import FilterSet
from apps.custom_models.students_models import Student



class StudentFilter(FilterSet):
    class Meta:
        model = Student
        fields = {
            'department':['exact'],
            'gender':['exact'], 
            # 'status':['exact'],
            'semester':['exact'],

        }
              