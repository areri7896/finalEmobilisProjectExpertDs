from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.http import HttpResponseRedirect


# Create your views here.
def dashboard(request):
    return render(request, 'portal/dashboard.html', {})


def login(request):
    return render(request, 'portal/login.html', {})


def messages(request):
    return render(request, 'portal/messages.html', {})


def reciept(request):
    return render(request, 'portal/reciept.html', {})


def payment(request):
    return render(request, 'portal/payfee.html', {})


def statement(request):
    return render(request, 'portal/statement.html', {})


def maps(request):
    return render(request, 'portal/map.html', {})


def settings(request):
    return render(request, 'portal/settings.html', {})


def profile(request):
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
    return render(request, 'portal/profile.html', {'form': form , 'submitted': submitted})


def admissions(request):
    return render(request, 'portal/personal.html', {})


def academics(request):
    return render(request, 'portal/academics.html', {})


def faqs(request):
    return render(request, 'portal/faqs.html', {})
