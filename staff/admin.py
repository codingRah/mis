from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Staff)
admin.site.register(models.StaffEducation)
admin.site.register(models.StaffExtraInfo)
admin.site.register(models.StaffJobExperience)
admin.site.register(models.StaffNationlityCartInfo)