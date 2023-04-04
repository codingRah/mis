from rest_framework import serializers
from .models import Student,StudentBulkUpload, StudentStatus, StudentNationlityCartInfo, StudentHostelService, StudentRelationContact
from accounts.serializers import UserSerializer

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Student
        fields = ['id','user','kankor_id','first_name','last_name','father_name','grand_father_name','school','score','department', 'gender','semester']


class StudentShortInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','first_name','last_name','father_name','department', 'gender','semester']


class StudentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentStatus
        fields = ['id','student','status']


class StudentsCartSerializer(serializers.ModelSerializer):
    class Meta:
        model  = StudentNationlityCartInfo
        fields = ['id','student','cart_type','cart_id','page_no','register_no','volume_no','front_image','back_image']
    
class StudentHostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentHostelService
        fields = ['id','student','service_type','wing_no','room_no']


class StudentRelationContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRelationContact
        fields = ['id','student','relation','relative_name','occupation','phone1','phone2']




class StudentBulkUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentBulkUpload
        fields = '__all__'