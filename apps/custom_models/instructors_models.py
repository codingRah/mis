from enum import unique
from django.db import models
from accounts.models import User
from .departments_models import Department
from accounts.models import UserAddress
from django.db.models.signals import post_save



class Staff(models.Model):
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, choices=GENDER)
    dob = models.DateField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to="staffs/avatar")

    def __str__(self):
        return self.first_name
    
def staff_profile_created(sender, instance, created, **kwargs):
    if created:
        user = instance
        staff_profile = Staff.objects.create(user=user, first_name = user.username)

post_save.connect(staff_profile_created, sender=User)            


class StaffNationlityCartInfo(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    cart_type = models.CharField(max_length=200)
    cart_id = models.CharField(max_length=200, unique=True)
    page_no = models.CharField(max_length=200, null=True, blank=True)
    register_no = models.CharField(max_length=200, null=True, blank=True)
    volume_no = models.CharField(max_length=200, null=True, blank=True)
    front_image = models.ImageField(upload_to="carts/", default="cart.jpg")
    back_image = models.ImageField(upload_to="carts/", default="cart.jpg")


    def __str__(self):
        return self.cart_id

class StaffExtraInfo(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=100)
    dieases = models.BooleanField(default=False)
    dieases_type = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.staff.first_name}'s detail info"


class StaffEducation(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    edu_title = models.CharField(max_length=200)
    uni_or_school = models.CharField(max_length=200)
    from_date = models.DateField(null=True,blank=True)
    to_date  = models.DateField(null=True, blank=True)
    ongoing = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to="staff/edu/", null=True, blank=True)


    def __str__(self):
        return f"{self.staff.first_name}'s {self.edu_title} education"


class StaffJobExperience(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    organization = models.TextField(max_length=200)
    position  = models.TextField(max_length=200)
    from_date = models.DateField(null=True, blank=True)
    to_date  = models.DateField(null=True, blank=True)
    ongoing = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to="staff/exper/", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.staff.first_name}'s {self.position} at {self.organization}"

