import datetime

from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.http import HttpResponseRedirect
from django.contrib import messages
import calendar
from calendar import HTMLCalendar
from datetime import datetime

from .models import Exam, Test, Statement


# Create your views here.
def dashboard(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    # create a calendar for dashboard
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(
        year,
        month_number,
    )
    now = datetime.now()
    current_year = now.year

    time = now.strftime('%I:%M %p')

    return render(request, 'portal/dashboard.html', {
        'month': month,
        'year': year,
        'month_number': month_number,
        'cal': cal,
        'time': time,
        'current_year': current_year,

    })


#
# def dashboard(request):
#     # create a calendar for dashboard
#     return render(request, 'portal/dashboard.html', {})


def login(request):
    return render(request, 'portal/login.html', {})


def messaging(request):
    return render(request, 'portal/messages.html', {})


def receipt(request):
    return render(request, 'portal/receipt.html', {})


def payment(request):
    return render(request, 'portal/payfee.html', {})


def statement(request):
    fee_statement = Statement.objects.all()
    context = {'fee_statement': fee_statement}
    return render(request, 'portal/statement.html', context)


def maps(request):
    return render(request, 'portal/map.html', {})


def settings(request):
    return render(request, 'portal/settings.html', {})


def edit_profile(request):
    submitted = False
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile?submitted=True')
    else:
        form = ProfileForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'portal/edit_profile.html', {'form': form, 'submitted': submitted})


def profile(request):
    # profile
    return render(request, 'portal/profile.html', {})


def admissions(request):
    return render(request, 'portal/book_exam.html', {})


def academics(request):
    return render(request, 'portal/academics.html', {})


def book_exam(request):
    if request.method == 'POST':
        exam_name = request.POST['exam']
        exam_date = request.POST['exam-date']
        exam_time = request.POST['exam-time']
        exam_venue = request.POST['exam-venue']

        data = Exam(exam_name=exam_name, exam_date=exam_date, exam_time=exam_time, exam_venue=exam_venue)
        data.save()
        messages.success(request, 'Booking saved successfully')
        return redirect('book-exam-url')
    return render(request, 'portal/academics.html', {})


def delete_exam(request, id):
    exam = Exam.objects.get(id=id)
    exam.delete()
    messages.success(request, 'Your booking was deleted successfully')
    return redirect('book-exam-url')


def exams(request):
    all_exams = Exam.objects.all()
    context = {"exams_list": all_exams}
    return render(request, 'portal/academics.html', context)


def test(request):
    all_tests = Test.objects.all()
    context = {"Test": all_tests}
    return render(request, 'portal/academics.html', context)


def book_test(request):
    if request.method == 'POST':
        test_name = request.POST['test-name']
        test_date = request.POST['test-date']
        test_time = request.POST['test-time']
        test_venue = request.POST['test-venue']

        data = Test(test_name=test_name, test_date=test_date, test_time=test_time, test_venue=test_venue)
        data.save()
        messages.success(request, 'Booking saved successfully')
        return redirect('book-test-url')
    return render(request, 'portal/academics.html', {})


def faqs(request):
    return render(request, 'portal/faqs.html', {})
