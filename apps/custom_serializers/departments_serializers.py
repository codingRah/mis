from rest_framework import serializers
from apps.custom_models.departments_models import Department, DepartmentChief, DepartmentProgramLevel, Semester
from .instructor_serializers import InstructorSerializer



class DepartmentChiefSerilizer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentChief
        fields = ['id','department','user','from_date','to_date']


class DepartmentSerializer(serializers.ModelSerializer):
    dep_chief = serializers.SerializerMethodField(read_only=True)
    instructors = serializers.SerializerMethodField(read_only=True)
    total_students = serializers.SerializerMethodField(read_only=True)
    total_active_students = serializers.SerializerMethodField(read_only=True)
    total_new_students = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Department
        fields = ['id','name','description','slug','code','status','created_at','dep_chief','instructors','total_students','total_active_students','total_new_students']
    
    def get_dep_chief(self,obj):
        data = obj.departmentchief_set.all()
        return DepartmentChiefSerilizer(data,many=True).data
    
    def get_instructors(self,obj):
        data = obj.staff_set.all()
        return InstructorSerializer(data, many=True).data
    
    def get_total_students(self, obj):
        pass

    def get_total_active_students(self,obj):
        pass

    def get_total_new_students(self, obj):
        pass

class DepartmentProgramLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentProgramLevel
        fields = ['id','department','level']
        
        
class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ['id','program','semester_number','semester_name']
