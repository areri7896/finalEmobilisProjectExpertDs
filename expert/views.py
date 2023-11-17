from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'expt/index.html', {})

def team(request):
    return render(request, 'expt/team.html', {})
def about(request):
    return render(request, 'expt/about.html', {})

def courses(request):
    return render(request, 'expt/courses.html', {})
def feature(request):
    return render(request, 'expt/feature.html', {})

def appointment(request):
    return render(request, 'expt/appointment.html', {})

def error(request):
    return render(request, 'expt/404.html', {})

def contact(request):
    return render(request, 'expt/contact.html', {})
def testimonial(request):
    return render(request, 'expt/testimonial.html', {})

