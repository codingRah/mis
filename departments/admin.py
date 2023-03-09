from django.contrib import admin
from .models import Department,DepartmentChief , DepartmentProgramLevel,Semester, Subject
# Register your models here.


admin.site.register(Department)
admin.site.register(DepartmentChief)
admin.site.register(DepartmentProgramLevel)
admin.site.register(Semester)
admin.site.register(Subject)

