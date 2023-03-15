from django.db import models
from departments.models import Department, Semester, Subject
from course.models import Session
from staff.models import Staff
# Create your models here.

class Schedule(models.Model):
    
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True, blank=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    instructor = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, blank=True)
    days = models.CharField(max_length=250)
    hours = models.CharField(max_length=250)
    from_time = models.TimeField()
    to_time = models.TimeField()

    def __str__(self):
        return self.days