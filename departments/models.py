from django.db import models
from accounts.models import User
from django.utils.text import slugify
import string
import random
# Create your models here.

def random_slug():
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(10))

class Department(models.Model):
    STATUS = (
        ("فعال", "فعال"),
        ("غیر فعال", "غیر فعال"),
    )
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    slug  = models.SlugField(max_length=200, unique=True)
    status = models.CharField(choices=STATUS, default="فعال", max_length=20)
    code = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(random_slug())
        super(Department, self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    

class DepartmentChief(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True)
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.department.name}'s chief "


class DepartmentProgramLevel(models.Model):
    # ? some departments might cover the master and phd programs too.
    # ?? So, we consider this case for programs beyond bachelor programs.
    # ??? default level is bachelor. We can also add master and doctorate programs 2
    STATUS_LEVEL = (
        ("لیسانس","لیسانس"),
        ("ماستری","ماستری"),
        ("دکترا","دکترا"),
    )
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    level = models.CharField(max_length=100, choices=STATUS_LEVEL,default="لیسانس") # default level is bachelor 

    def __str__(self):
        return self.level


class Semester(models.Model):
    # ? based on specific program, the length of semester changes.
    # ?? For instance, bachelor program contains 8 semsters, MA and PHD 4
    program  = models.ForeignKey(DepartmentProgramLevel, on_delete=models.CASCADE, null=True, blank=True)
    semester_number = models.SmallIntegerField(default=1)
    semester_name   = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.semester_name} for {self.program.level}' program"


class Subject(models.Model):
    name = models.CharField(max_length=200)
    credit = models.PositiveSmallIntegerField(default=1)
    subject_type = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    slug  = models.SlugField(max_length=200, unique=True)
    code = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(random_slug() + "-" + self.name)
        super(Subject, self).save(*args,**kwargs)

    def __str__(self):
        return self.name