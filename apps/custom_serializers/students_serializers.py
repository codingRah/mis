from rest_framework import serializers
from apps.custom_models.students_models import Student, StudentStatus, StudentNationlityCartInfo, StudentHostelService, StudentRelationContact


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','user','kankor_id','first_name','last_name','father_name','grand_father_name','school','score','department', 'gender','semester','image']


class StudentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentStatus
        fields = ['id','student','status']


class StudentsCartSerializer(serializers.ModelSerializer):
    pass

