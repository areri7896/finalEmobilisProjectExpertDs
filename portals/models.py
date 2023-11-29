from django.db import models
from django.contrib.auth.models import User, UserManager


# Create your models here.
class Result(models.Model):
    course_name = models.CharField(max_length=10)
    marks = models.IntegerField()
    grade = models.CharField(max_length=10)
    comment = models.CharField(max_length=10)
    supervisor = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.course_name


class Location(models.Model):
    county = models.CharField(max_length=50, default=' ')
    constituency = models.CharField(max_length=50, default=' ')
    ward = models.CharField(max_length=50, default=' ')
    location = models.CharField(max_length=50, null=True)
    sub_location = models.CharField(max_length=50, null=True)
    village = models.CharField(max_length=50, null=True)
    box_no = models.IntegerField
    postal_codee = models.IntegerField
    town = models.CharField(max_length=50, default=' ')

    def __str__(self):
        return self.county


class Student(models.Model):
    first_name = models.CharField(max_length=50, default=' ')
    surname = models.CharField(max_length=50, default=' ')
    other_names = models.CharField(max_length=50, default=' ')
    regno = models.CharField(max_length=10, unique=True)
    course = models.CharField(max_length=15, default=' ')

    def __str__(self):
        return self.first_name


class Profile(models.Model):
    id_no = models.IntegerField(blank=True)
    email = models.EmailField(max_length=50)
    phone_number = models.IntegerField()
    gender = models.CharField(max_length=50, null=True)
    address = models.ManyToManyField(Location, blank=True)


class Exam(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    exam_name = models.CharField(max_length=50, null=False)
    exam_date = models.CharField(max_length=50, null=False)
    exam_time = models.CharField(max_length=50, null=False)
    exam_venue = models.CharField(max_length=10, blank=False, null=False)
    supervisor = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.exam_name}"


class Test(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    test_name = models.CharField(max_length=50, blank=False, null=False)
    test_date = models.CharField(max_length=50, null=False)
    test_time = models.CharField(max_length=50, null=False)
    test_venue = models.CharField(max_length=10, blank=False, null=False)
    supervisor = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.test_name


class Statement(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    ref = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=50)
    debit = models.IntegerField()
    credit = models.IntegerField()
    balance = models.IntegerField()

    def __str__(self):
        return self.description
