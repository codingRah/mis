from django.db import models
from accounts.models import User
from django.utils.text import slugify
import string
import random
import uuid
# Create your models here.

class Department(models.Model):
    STATUS = (
        ("فعال", "فعال"),
        ("غیر فعال", "غیر فعال"),
    )
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    slug  = models.SlugField(max_length=200, unique=True, editable=False)
    status = models.CharField(choices=STATUS, default="فعال", max_length=20)
    code = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(uuid.uuid4()))
        super(Department, self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    

class DepartmentChief(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True)
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.department.name}'s chief "


class DepartmentProgramLevel(models.Model):

    STATUS_LEVEL = (
        ("لیسانس","لیسانس"),
        ("ماستری","ماستری"),
        ("دکترا","دکترا"),
    )
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    level = models.CharField(max_length=100, choices=STATUS_LEVEL,default="لیسانس") # default level is bachelor 

    def __str__(self):
        return f"{self.level} in department {self.department}"


class Semester(models.Model):
    program  = models.ForeignKey(DepartmentProgramLevel, on_delete=models.CASCADE, null=True, blank=True)
    semester_number = models.SmallIntegerField(default=1)
    semester_name   = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.semester_name}"


class Subject(models.Model):
    name = models.CharField(max_length=200)
    credit = models.PositiveSmallIntegerField(default=1)
    subject_type = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    slug  = models.SlugField(max_length=200, unique=True, editable=False)
    code = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(uuid.uuid4()))
        super(Subject, self).save(*args,**kwargs)

    def __str__(self):
        return self.name