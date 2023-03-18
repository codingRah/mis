from rest_framework import serializers
from .models import Department, DepartmentChief, DepartmentProgramLevel, Semester
from staff.models import Staff
from accounts.serializers import UserSerializer
from accounts.models import User
from students.serializers import StudentSerializer, StudentStatusSerializer
from staff.serializers import InstructorSerializer
from .models import Subject

class UserShortInforSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]

class DepartmentChiefSerilizer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = DepartmentChief
        fields = ['id','department','user','from_date','to_date']


    def get_user(self, obj):
        data = obj.user
        return UserShortInforSerializer(data, many=False).data


class DepartmentSerializer(serializers.ModelSerializer):
    dep_chief = serializers.SerializerMethodField(read_only=True)
    instructors = serializers.SerializerMethodField(read_only=True)
    total_students = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Department
        fields = ['id','name','description','slug','code','status','created_at','instructors','dep_chief','total_students']
    
    def get_dep_chief(self,obj):
        data = obj.departmentchief_set.all()
        return DepartmentChiefSerilizer(data,many=True).data
    
    def get_instructors(self,obj):
        data = obj.staff_set.all()
        return InstructorSerializer(data, many=True).data
    
    def get_total_students(self, obj):
        data = obj.student_set.all()
        return StudentSerializer(data, many=True).data

    

class DepartmentProgramLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentProgramLevel
        fields = ['id','department','level']
        
        
class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ['id','program','semester_number','semester_name']


class SubjectSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField(read_only=True)
    semester = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Subject
        fields = ['id','name','credit','subject_type','slug','description','code','department','semester']

    def get_department(self, obj):
        data = obj.department
        return DepartmentSerializer(data, many=False).data

    def get_semester(self, obj):
        data = obj.semester
        return SemesterSerializer(data, many=False).data
    
class SubjectShortInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name','credit']