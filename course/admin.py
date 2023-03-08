from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Course)
admin.site.register(models.Session)
admin.site.register(models.ContentType)
admin.site.register(models.Content)
admin.site.register(models.CourseDetail)
admin.site.register(models.CourseEvent)
admin.site.register(models.CourseStatus)
admin.site.register(models.Module)

