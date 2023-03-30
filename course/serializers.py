from rest_framework import serializers
from .models import *
from accounts.serializers import StaffShortInfoSerializer
from departments.models import Subject
from departments.serializers import SubjectShortInfoSerializer, SemesterSerializer
from students.serializers import StudentShortInfoSerializer


class SessionShortInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = [
            'id', 
            'session_type', 
            'session_start_date',
            'session_duration'
        ]



class CourseSerializer(serializers.ModelSerializer):
    owner = StaffShortInfoSerializer(read_only=True)
    session = SessionShortInfoSerializer(read_only=True)
    subject = SubjectShortInfoSerializer(read_only=True)
    student = StudentShortInfoSerializer(read_only=True)
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
            'student',
            'title', 
            'description', 
            'created_at', 
            'updated_at'
            # 'modules', 
            # 'detail', 
            # 'status'
        ]
    # def get_modules(self, obj):
    #     modules = obj.module_set.all()
    #     return ModuleSerializer(modules, many=True).data

    # def get_detail(self, obj):
    #     detail = obj.coursedetail
    #     return CourseDetailSerializer(detail, many=False).data

    # def get_status(self, obj):
    #     status = obj.coursestatus
    #     return CourseStatusSerializer(status, many=False).data



class CourseDetailSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=False, read_only=True)
    class Meta:
        model = CourseDetail
        fields = [
            "id",'image', 'color', 'course'
        ]

class CourseStatusSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=False, read_only=True)
    class Meta:
        model = CourseStatus
        fields = [
            'id', 'status', 'course'
        ]


class ModuleSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=False, read_only=True)
    class Meta:
        model = Module
        fields = [
            'id',
            'week', 
            'title', 
            'description', 
            'created_at', 
            'updated_at', 
            'course'
        ]

    # def get_contents(self, obj):
    #     data = obj.content_set.all()
    #     return ContentSerializer(data, many=True).data


class ContentSerializer(serializers.ModelSerializer):
    module = ModuleSerializer(many=False, read_only=True)
    class Meta:
        model = Content
        fields = [
            'id', 
            'title', 
            'description', 
            'created_at', 
            'updated_at', 
            'module'
        ]


class ContentTypeSerializer(serializers.ModelSerializer):
    content = ContentSerializer(many=False, read_only=True)
    class Meta:
        model = ContentType
        fields = [
            'id', 'url', 'file', 'image','content'
        ]

 



class SubjectShortInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id','name', 'credit']


class CourseEventSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=False, read_only=True)
    class Meta:
        model = CourseEvent
        fields = ['id','course','title','description','start_at','end_at']




class SessionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Session
        fields = [
            'id', 
            "session_type", 
            "session_duration",
            "description", 
            "session_start_date", 
            "session_end_date", 
            "status", 
            "created_at", 
            "updated_at"
        ]
        
    # def get_courses(self, obj):
    #     data = obj.course_set.all()
    #     return CourseSerializer(data, many=True).data

# serialize subject assignment to instrucot

class SubjectAssignmentToInstructorSerializer(serializers.ModelSerializer):
    instructor = StaffShortInfoSerializer(many=True, read_only=True)
    subject = serializers.SerializerMethodField(read_only=True)
    session = serializers.SerializerMethodField(read_only=True)
    semester = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = SubjectAssignmentToInstructor
        fields = [
            'instructor', 
            'subject', 
            'session', 
            'semester', 
            'created_at', 
            'updated_at'
        ]
    # def get_instructor(self, obj):
    #     data = obj.instructor
    #     return StaffShortInfoSerializer(data, many=False).data

    def get_subject(self, obj):
        data = obj.subject
        return SubjectShortInfoSerializer(data, many=False).data
    
    def get_session(self, obj):
        data = obj.session
        return SessionShortInfoSerializer(data, many=False).data
    
    def get_semester(self, obj):
        data = obj.semester
        return SemesterSerializer(data, many=False).data