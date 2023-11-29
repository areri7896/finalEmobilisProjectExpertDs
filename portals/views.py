import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileForm, SignUpForm, TestForm, ExamForm
from django.http import HttpResponseRedirect
from django.contrib import messages
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from .models import Exam, Test, Statement, Result


# Create your views here.
def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "you have been successfully registered")
            return redirect('dashboard')

    else:
        form = SignUpForm()
        return render(request, 'portal/register.html', {'form': form})
    return render(request, 'portal/register.html', {'form': form})


@login_required
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


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out Successfully !!!')
    return render(request, 'portal/login.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['Password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Your Have Been Successfully Logged in')
            return redirect('dashboard')
        else:
            messages.success(request, 'There was an error logging in. please check your credentials amd try again!!')
    else:
        return render(request, 'portal/login.html', {})


@login_required
def messaging(request):
    return render(request, 'portal/messages.html', {})


@login_required
def receipt(request):
    return render(request, 'portal/receipt.html', {})


@login_required
def payment(request):
    return render(request, 'portal/payfee.html', {})


@login_required
def statement(request):
    fee_statement = Statement.objects.all()
    context = {'fee_statement': fee_statement}
    return render(request, 'portal/statement.html', context)


def statement_pdf(request):
    buff = io.BytesIO()
    c = canvas.Canvas(buff, pagesize=letter, bottomup=0)
    textobject = c.beginText()
    textobject.setTextOrigin(inch, inch)
    textobject.setFont('Helvetica', 14)

    records = Statement.objects.all()

    lines = [
        "record.date",
        "record.ref",
        "record.description",
    ]
    for record in records:
        lines.append(record)

        # for row in row:
        #     textobject.textLine(row)

        c.drawText(textobject)
        c.showPage()
        c.save()
        buff.seek(0)
    return FileResponse(buff, as_attachment=True, filename='statement.pdf')


@login_required
def maps(request):
    return render(request, 'portal/map.html', {})


@login_required
def settings(request):
    return render(request, 'portal/settings.html', {})


@login_required
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


@login_required
def profile(request):
    # profile
    return render(request, 'portal/profile.html', {})


@login_required
def result(request):
    results = Result.objects.all()
    return render(request, 'portal/results.html', {'results': results})


@login_required
def academics(request):
    return render(request, 'portal/academics.html', {})


@login_required
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


@login_required
def delete_test(request, id):
    if request.user.is_authenticated:
        testbooking = Test.objects.get(id=id)
        testbooking.delete()
        messages.success(request, 'Your booking was deleted successfully')
        return redirect('test-booking-url')
    else:
        messages.success(request, 'SORRY!!!!, you have to be logged in to update this record')
        return redirect('login_user-url')


@login_required
def delete_exam(request, pk):
    examination = Exam.objects.get(id=pk)
    examination.delete()
    messages.success(request, 'Your booking was deleted successfully')
    return redirect('exam-booking-url')


def exam_update(request, pk):
    if request.user.is_authenticated:
        current_exam_record = Exam.objects.get(id=pk)
        form = ExamForm(request.POST or None, instance=current_exam_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'your record was successfuly updated')
            return redirect('exam-booking-url')
        return render(request, 'portal/edit_exam.html', {'current_exam_form': form})
    else:
        messages.success(request, 'SORRY!!!!, you have to be logged in to update this record')
    return redirect('exam-booking-url')


def edit_test(request, pk):
    if request.user.is_authenticated:
        current_test_record = Test.objects.get(id=pk)
        form = TestForm(request.POST or None, instance=current_test_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'your record was successfuly updated')
            return redirect('test-booking-url')
        return render(request, 'portal/edit_test.html', {'current_test_form': form})
    else:
        messages.success(request, 'SORRY!!!!, you have to be logged in to update this record')
        return redirect('test-booking-url')


@login_required
def exam_record(request):
    all_exams = Exam.objects.all()
    return render(request, 'portal/exam-bookings.html', {'all_exams': all_exams})


@login_required
def test_record(request):
    all_tests = Test.objects.all()
    return render(request, 'portal/tets-bookings.html', {'all_tests': all_tests})


@login_required
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


@login_required
def faqs(request):
    return render(request, 'portal/faqs.html', {})
