from rest_framework import serializers
from . import models
from departments.serializers import SubjectSerializer
from students.serializers import StudentSerializer

class ResultSerializer(serializers.ModelSerializer):
    subject = serializers.SerializerMethodField(read_only=True)
    student = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = models.Result
        fields = ['id', 'subject', 'student', 'class_activity', 'assignment', 'mid_term', 'final', 'project', 'is_pass', 'chances']

    def get_subject(self, obj):
        data = obj.subject_set.all()
        return SubjectSerializer(data, many=True).data
    
    def get_student(self, obj):
        data = obj.student_set.all()
        return StudentSerializer(data, many=True).data
    
    
class ResultBulkUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ResultBulkUpload
        fields = '__all__'    
        
class CourseResultBulkUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseResultUpload
        fields = '__all__'