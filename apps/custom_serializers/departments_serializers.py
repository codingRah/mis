from rest_framework import serializers
from apps.custom_models.departments_models import Department, DepartmentChief, DepartmentProgramLevel, Semester


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["id", "name", "slug", "description", "code", "created_at"]
        

class DepartmentChiefSerilizer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentChief
        fields = '__all__'
        
        
class DepartmentProgramLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentProgramLevel
        fields = '__all__'
        
        
class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'
