from rest_framework import serializers
from .models import *
from accounts.serializers import StaffShortInfoSerializer
from departments.models import Subject


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDetail
        fields = [
            "id",'image', 'color', 'course'
        ]

class CourseStatusSerializer(serializers.ModelSerializer):
    # course = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = CourseStatus
        fields = [
            'id', 'status', 'course'
        ]

class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = [
            'id', 'url', 'file', 'image','content'
        ]

    
class ContentSerializer(serializers.ModelSerializer):
    content_types = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Content
        fields = [
            'id', 
            'title', 
            'description', 
            'created_at', 
            'updated_at', 
            'content_types'
        ]

    def get_content_types(self, obj):
        data = obj.contenttype_set.all()
        return ContentTypeSerializer(data, many=True).data

class ModuleSerializer(serializers.ModelSerializer):
    contents = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Module
        fields = [
            'id',
            'week', 
            'title', 
            'description', 
            'created_at', 
            'updated_at', 
            "contents",
            'course'
        ]

    def get_contents(self, obj):
        data = obj.content_set.all()
        return ContentSerializer(data, many=True).data


class SessionShortInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = [
            'id', 
            'session_type', 
            'session_start_date'
        ]


class SubjectShortInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id','name', 'credit']


class CourseEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEvent
        fields = ['id','course','title','description','start_at','end_at']

class CourseSerializer(serializers.ModelSerializer):
    owner = StaffShortInfoSerializer(read_only=True)
    session = SessionShortInfoSerializer(read_only=True)
    subject = SubjectShortInfoSerializer(read_only=True)
    # modules = serializers.SerializerMethodField()
    # detail = serializers.SerializerMethodField()
    # status  = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Course
        fields = [
            'id', 
            'owner', 
            'session',
            'subject',
            'code', 
            'title', 
            'slug', 
            'description', 
            'created_at', 
            'updated_at', 
            # 'modules', 
            # 'detail', 
            # 'status'
        ]
        
    def get_owner(self, obj):
        data = obj.owner_set.all()
        return StaffShortInfoSerializer(data, many=True).data

    # def get_modules(self, obj):
    #     modules = obj.module_set.all()
    #     return ModuleSerializer(modules, many=True).data

    # def get_detail(self, obj):
    #     detail = obj.coursedetail
    #     return CourseDetailSerializer(detail, many=False).data

    # def get_status(self, obj):
    #     status = obj.coursestatus
    #     return CourseStatusSerializer(status, many=False).data



class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = [
            'id', 
            "session_type", 
            "description", 
            "session_start_date", 
            "session_end_date", 
            "status", 
            "created_at", 
            "updated_at"
        ]

