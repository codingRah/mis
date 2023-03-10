from django.db import models
from students.models import Student
from staff.models import Staff
from departments.models import Subject, Semester
from django.utils import timezone
from django.utils.text import slugify
import string
import random
# Create your models here.

def course_random_slug():
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(30))


def generate_course_code():
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(10))


class SubjectAssignmentToInstructor(models.Model):
    instructor = models.ForeignKey(Staff, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    session = models.ForeignKey("Session", on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subject.name} assigned to {self.instructor.first_name}"



class Session(models.Model):
    session_type = models.CharField(max_length=100) # session type like session fall 2022 or session spring 2022
    description = models.TextField(null=True, blank=True)
    session_start_date = models.DateField()
    session_end_date = models.DateField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at  = models.DateField(auto_now=True)

    def __str__(self):
        return self.session_type




class Course(models.Model):
    owner = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    session = models.ForeignKey(Session, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    students  = models.ManyToManyField(Student, related_name="join_course", blank=True)
    code = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(course_random_slug())

        if not self.code:
            self.code = slugify(generate_course_code())
    
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class CourseStatus(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.course.title}'s status"


class CourseDetail(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="course/bg/", null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.course.title}'s detail"


class CourseEvent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    start_at = models.DateTimeField(auto_now_add=True)
    end_at= models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.course.title}' event"


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    week = models.PositiveSmallIntegerField(default=1)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.course}'s module "


class Content(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

class ContentType(models.Model):

    content = models.ForeignKey(Content, on_delete=models.CASCADE,null=True, blank=True)

    url = models.URLField(max_length=200, null=True, blank=True)
    file = models.FileField(upload_to="course/content", null=True, blank=True)
    image = models.ImageField(upload_to='course/content', null=True, blank=True)

    def __str__(self):
        return f"{self.content.title}'s type"
