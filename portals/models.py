from django.db import models


# Create your models here.
class Profile(models.Model):
    surname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    other_names = models.CharField(max_length=50)
    id_number = models.IntegerField()
    email = models.EmailField(max_length=50)
    phone_number = models.IntegerField()
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.surname + ' ' + self.firstname


class Address(models.Model):
    county = models.CharField(max_length=50)
    constituency = models.CharField(max_length=50)
    ward = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    sub_location = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    box_no = models.IntegerField
    postal_codee = models.IntegerField
    town = models.CharField(max_length=50)

    def __str__(self):
        return self.county
