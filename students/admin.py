from django.contrib import admin
from .models import Student, StudentHostelService, StudentNationlityCartInfo, StudentRelationContact,StudentStatus

admin.site.register(Student)
admin.site.register(StudentHostelService)
admin.site.register(StudentNationlityCartInfo)
admin.site.register(StudentRelationContact)
admin.site.register(StudentStatus)