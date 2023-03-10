from django.db import models

# Create your models here.
from pyexpat import model
from django.db import models
from course.models import Course
from students.models import Student
from departments.models import Subject
from .utils import score_grade
# Create your models here.

class Result(models.Model):
    CHANCES = (
        ("اول", "اول"),
        ("دوم", "دوم"),
        ("سوم", "سوم"),
        ("چهارم", "چهارم"),
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_activity = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    assignment = models.DecimalField(max_digits=4, decimal_places=2,default=0.0)
    mid_term = models.DecimalField(max_digits=4, decimal_places=2,default=0.0)
    final = models.DecimalField(max_digits=4, decimal_places=2,default=0.0)
    project = models.DecimalField(max_digits=4, decimal_places=2,default=0.0)
    is_pass = models.BooleanField(default=False)
    chances = models.CharField(max_length=20, choices=CHANCES, default="اول")
    present = models.CharField(max_length=200)
    absent = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.is_pass:
            if self.class_activity + self.assignment + self.mid_term + self.final + self.project >= 55:
                self.is_pass = True
            else:
                self.is_pass = False
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ["subject"]

    def __str__(self):
        return f"{self.student.user.username}'s grade from {self.subject.name} subject "

    def total_score(self):
        return self.class_activity + self.assignment + self.mid_term + self.final + self.project


    def activity_score(self):
        return self.class_activity + self.assignment + self.project

    def grade(self):
        return score_grade(self.total_score())



class ResultBulkUpload(models.Model):
    csv_file = models.FileField(upload_to="result/bulk/")
    uploaded_at = models.DateTimeField(auto_now_add=True)




class CourseResultUpload(models.Model):
    csv_file = models.FileField(upload_to="course/result/upload")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"file {self.csv_file}"

