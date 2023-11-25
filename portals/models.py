from django.db import models


# Create your models here.


class Location(models.Model):
    county = models.CharField(max_length=50, default='Nairobi')
    constituency = models.CharField(max_length=50, default='Embakasi')
    ward = models.CharField(max_length=50, default='CBD')
    location = models.CharField(max_length=50, null=True)
    sub_location = models.CharField(max_length=50, null=True)
    village = models.CharField(max_length=50, null=True)
    box_no = models.IntegerField
    postal_codee = models.IntegerField
    town = models.CharField(max_length=50, default='Nakuru')

    def __str__(self):
        return self.county


class Profile(models.Model):
    id_number = models.IntegerField()
    email = models.EmailField(max_length=50)
    phone_number = models.IntegerField()
    gender = models.CharField(max_length=50, null=True)
    address = models.ManyToManyField(Location, blank=True)


class Student(models.Model):
    first_name = models.CharField(max_length=50, default='John')
    surname = models.CharField(max_length=50, default='Doe')
    other_names = models.CharField(max_length=50, default='your_default_value')
    regno = models.CharField(max_length=10, unique=True)
    course = models.CharField(max_length=15, default=' Class B')
    profile = models.ForeignKey(Profile, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.regno + ' ' + self.first_name


class Exam(models.Model):
    exam_name = models.CharField(max_length=50, null=False)
    exam_date = models.CharField(max_length=50, null=False)
    exam_time = models.CharField(max_length=50, null=False)
    exam_venue = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.exam_name



class Test(models.Model):
    test_name = models.CharField(max_length=50, blank=False, null=False)
    test_date = models.CharField(max_length=50, null=False)
    test_time = models.CharField(max_length=50, null=False)
    test_venue = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.test_name
