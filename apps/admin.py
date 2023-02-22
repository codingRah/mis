from django.contrib import admin
from apps.custom_models import departments_models, instructors_models, students_models
# Register your models here.

admin.site.register(departments_models.Department)
admin.site.register(departments_models.DepartmentChief)
admin.site.register(departments_models.DepartmentProgramLevel)
admin.site.register(departments_models.Semester)

# admin.site.register(students_models.Student)

# admin for instructor model
admin.site.register(instructors_models.Staff)
admin.site.register(instructors_models.StaffEducation)
admin.site.register(instructors_models.StaffExtraInfo)
admin.site.register(instructors_models.StaffJobExperience)
admin.site.register(instructors_models.StaffNationlityCartInfo)
