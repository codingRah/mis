from rest_framework import serializers
from apps.custom_models import instructors_models

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = instructors_models.Staff
        fields = ['id', 'user', 'first_name','last_name','father_name','gender','dob','department','bio','phone','image']
 
        
class InstructorNationalityCartInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = instructors_models.StaffNationlityCartInfo
        fields = ['id','staff','cart_type','cart_id','page_no','register_no','volume_no','front_image','back_image']        
        

class InstructorEductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = instructors_models.StaffEducation
        fields = ['id','staff','edu_title','uni_or_school','from_date','to_date','ongoing','description','file']        
  
        
class InstructorExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = instructors_models.StaffJobExperience
        fields = ['id','staff','organization','position','from_date','to_date','ongoing','description','file']        
        
        
class InstructorExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = instructors_models.StaffExtraInfo
        fields = ['id','staff','blood_group','dieases','dieases_type']        
                