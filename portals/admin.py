from django.contrib import admin
from .models import Test, Exam, Profile, Location, Student

# Register your models here.
admin.site.register(Student)
admin.site.register(Profile)
admin.site.register(Location)
admin.site.register(Test)
admin.site.register(Exam)
