from rest_framework import serializers
from . import models
from departments.serializers import SubjectSerializer
from students.serializers import StudentSerializer

class ResultSerializer(serializers.ModelSerializer):
    subject = serializers.SerializerMethodField(read_only=True)
    student = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = models.Result
        fields = ['id', 'subject', 'student', 'class_activity', 'assignment', 
                'mid_term', 'final', 'project', 'is_pass', 'chances','total_score','activity_score','grade']

    def get_subject(self, obj):
        data = obj.subject
        return SubjectSerializer(data).data
    
    def get_student(self, obj):
        data = obj.student
        return StudentSerializer(data).data
    
    
class ResultBulkUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ResultBulkUpload
        fields = '__all__'    
        
class CourseResultBulkUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseResultUpload
        fields = '__all__'