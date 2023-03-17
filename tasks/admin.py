from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Assignment)
admin.site.register(models.AssignmentScore)
admin.site.register(models.Respond)