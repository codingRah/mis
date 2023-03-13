from rest_framework import serializers
from . import models
from course.serializers import ContentSerializer
from students.serializers import StudentSerializer,StudentShortInfoSerializer
from accounts.serializers import UserSerializer

class AssignmentSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField(read_only=True)
    content = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = models.Assignment
        fields = [
            'id',
            'owner',
            'content',
            'title',
            'description',
            'file',
            'assigned_at',
            'expire_date',
            'expire_time',
            'score',
            'lock_after_expiration',
            'is_submitted'
            ]
        
    def get_owner(self, obj):
        data = obj.owner
        return UserSerializer(data, many=False).data
    
    def get_content(self, obj):
        data = obj.content
        return ContentSerializer(data, many=False).data


class RespondSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField(read_only=True)
    assignment = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = models.Respond
        fields = [
            'id',
            'sender',
            'assignment',
            'title',
            'description',
            'file',
            'difficulties',
            'respond_at'
            ]
        
    def get_sender(self, obj):
        data = obj.sender
        return StudentShortInfoSerializer(data, many=False).data
    
    def get_assignment(self, obj):
        data = obj.assignment
        return AssignmentSerializer(data, many=False).data
    
    
class AssignmentScoreSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField(read_only=True)
    assignment = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = models.AssignmentScore
        fields = ['id','student', 'assignment', 'score']    
        
    def get_student(self, obj):
        data = obj.student
        return StudentSerializer(data, many=False).data
    
    def get_assignment(self, obj):
        data = obj.assignment
        return AssignmentSerializer(data, many=False).data
    
    
        
            