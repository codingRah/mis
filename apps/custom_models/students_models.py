from django.db import models
from .departments_models import Department, Semester
from accounts.models import User
from django.db.models.signals import post_save


class Student(models.Model):
    GENDER = (
        ("آقا", "آقا"),
        ("خانم", "خانم"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    kankor_id = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    grand_father_name = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    score = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER ,default='آقا')
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="students/avatar", default='student.jpg')


    def __str__(self):
        return self.first_name

def student_profile_created(sender, instance, created, **kwargs):
    if created:
        user = instance
        student_profile = Student.objects.create(user=user, first_name = user.username)
post_save.connect(student_profile_created, sender=User)

class StudentStatus(models.Model):
    STATUS = (
        ("فعال", 'فعال'),
        ("چانس", 'چانس'),
        ("تعجیل", 'تعجیل'),
        ("منفک", 'منفک'),
    )
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default="فعال")

    def __str__(self):
        return f"{self.student.first_name} {self.status} status"


class StudentNationlityCartInfo(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    cart_type = models.CharField(max_length=200)
    cart_id = models.CharField(max_length=200, unique=True)
    page_no = models.CharField(max_length=200, null=True, blank=True)
    register_no = models.CharField(max_length=200, null=True, blank=True)
    volume_no = models.CharField(max_length=200, null=True, blank=True)
    front_image = models.ImageField(upload_to="carts/", default="cart.jpg")
    back_image = models.ImageField(upload_to="carts/", default="cart.jpg")


    def __str__(self):
        return self.cart_id


class StudentHostelService(models.Model):
    SERVICE = (
        ("Hostel", "Hostel"),
        ("Money", "Money"),
    )
    student  = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True)
    service_type = models.CharField(max_length=30, choices=SERVICE)
    wing_no = models.CharField(max_length=100, null=True, blank=True)
    room_no = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.student.first_name}'s service "


class StudentRelationContact(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    relation = models.CharField(max_length=200)
    relative_name = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.student.first_name}'s relations info"
