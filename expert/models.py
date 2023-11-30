from django.db import models


# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(unique=False, max_length=50)
    date = models.DateField()
    time = models.TimeField()
    pnumber = models.CharField(max_length=12)
    location = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=50, blank=True)
    subject = models.CharField(max_length=250)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Enquiry(models.Model):
    name = models.CharField(max_length=70)
    gmail = models.EmailField(max_length=50, blank=True)
    courses = models.CharField(max_length=70)
    vehicleclass = models.CharField(max_length=70)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

#
# class Subscribe(models.Model):
#     subscriber = models.EmailField(blank=True, max_length=50)
#
