from rest_framework import serializers
from . import models
from departments.serializers import SubjectSerializer
from students.serializers import StudentSerializer

class ResultSerializer(serializers.ModelField):
    subject = serializers.SerializerMethodField(read_only=True)
    student = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = models.Result
        fields = {'id', 'subject', 'student', 'class_activity', 'assignment', 'mid_term', 'final', 'project', 'is_pass', 'chances'}

    def get_subject(self, obj):
        data = obj.subject_set.all()
        return SubjectSerializer(data, many=True).data
    
    def get_student(self, obj):
        data = obj.student.all()
        return StudentSerializer(data, many=True).data
    
    
class ResultBulkUploadSerializer(serializers.ModelField):
    class Meta:
        model = models.ResultBulkUpload
        fields = '__all__'    
        
class CourseResultBulkUploadSerializer(serializers.ModelField):
    class Meta:
        model = models.CourseResultUpload
        fields = '__all__'