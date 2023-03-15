from rest_framework import serializers
from . import models
from departments.serializers import SubjectShortInfoSerializer, DepartmentSerializer
from course.serializers import SessionShortInfoSerializer,SemesterSerializer
from staff.serializers import InstructorSerializer


class ScheduleSerializer(serializers.ModelSerializer):
    
    department = serializers.SerializerMethodField(read_only=True)
    semester = serializers.SerializerMethodField(read_only=True)
    subject = serializers.SerializerMethodField(read_only=True)
    instructor = serializers.SerializerMethodField(read_only=True)
    session = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = models.Schedule
        fields = [
            'department',
            'semester',
            'session',
            'subject',
            'instructor',
            'days',
            'hours',
            'from_time',
            'to_time',
        ]
    
    def get_department(self, obj):
        data = obj.department
        return DepartmentSerializer(data, many=False).data    
    
    def get_semester(self, obj):
        data = obj.semester
        return SemesterSerializer(data, many=False).data    
    
    def get_session(self, obj):
        data = obj.session
        return SessionShortInfoSerializer(data, many=False).data    
    
    def get_subject(self, obj):
        data = obj.subject
        return SubjectShortInfoSerializer(data, many=False).data    
    
    def get_instructor(self, obj):
        data = obj.instructor
        return InstructorSerializer(data, many=False).data    
                