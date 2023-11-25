from django.contrib import admin
from .models import Test, Exam, Profile, Location, Student, Statement, Result

# Register your models here.
admin.site.register(Student)
admin.site.register(Profile)
admin.site.register(Location)


# admin.site.register(Test)
# admin.site.register(Exam)
# admin.site.register(Statement)
# admin.site.register(Result)

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('exam_name', 'exam_time', 'exam_venue')
    ordering = ('exam_date',)
    search_fields = ('exam_venue', 'exam_date', 'exam_name')


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('test_time', 'test_venue')
    ordering = ('test_date',)
    search_fields = ('test_date', 'test_venue', 'test_name')


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'marks', 'grade', 'comment',)
    ordering = ('marks',)
    search_fields = ('comment', 'marks')


@admin.register(Statement)
class StatementAdmin(admin.ModelAdmin):
    list_display = ('date', 'ref', 'description', 'debit', 'credit', 'balance',)
    ordering = ('date',)
    search_fields = ('ref', 'description', 'balance', 'date',)
