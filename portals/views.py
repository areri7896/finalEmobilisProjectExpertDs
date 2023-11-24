from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import Exam, Test


# Create your views here.
def dashboard(request):
    return render(request, 'portal/dashboard.html', {})


def login(request):
    return render(request, 'portal/login.html', {})


def messages(request):
    return render(request, 'portal/messages.html', {})


def receipt(request):
    return render(request, 'portal/receipt.html', {})


def payment(request):
    return render(request, 'portal/payfee.html', {})


def statement(request):
    return render(request, 'portal/statement.html', {})


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
        exam = request.POST.get('exam-name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        venue = request.POST.get('venue')

        data = Exam(exam=exam, date=date, time=time, venue=venue)
        data.save()
        messages.success(request, "Product saved successfully")
        return redirect("book-exam-url")
    return render(request, 'portal/academics.html', {})


def book_test(request):
    if request.method == 'POST':
        test_name = request.POST.get('test-name')
        date = request.POST.get('test-date')
        time = request.POST.get('test-time')
        venue = request.POST.get('test-venue')

        data = Test(test_name=test_name, date=date, time=time, venue=venue)
        data.save()
        messages.success(request, "Product saved successfully")
        return redirect("book-test-url")
    return render(request, 'portal/academics.html', {})


def faqs(request):
    return render(request, 'portal/faqs.html', {})
