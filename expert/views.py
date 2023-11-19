from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST['gname']
        email = request.POST['gmail']
        cname = request.POST['cname']
        vehicle = request.POST['vehicle']
        message = request.POST['message']

        # send email
        send_mail(
            cname + ' ' + name,  # subject,
            message + vehicle,  # message,
            email,  # from email,
            ['expertyomo62@gmail.com', ' expertprint02@gmail.com'],  # to email
        )
        return render(request, 'expt/index.html', {'name': name})
    else:
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
    if request.method != "POST":
        name = request.POST['name']
        email = request.POST['gemail']
        date = request.POST['date']
        time = request.POST['time']
        phone = request.POST['phone']
        location = request.POST['location']
        message = request.POST['message']

        return render(request, 'expt/appointment.html', {'name': name, 'phone': phone})
    else:
        return render(request, 'expt/appointment.html', {})


def error(request):
    return render(request, 'expt/404.html', {})


def contact(request):
    if request.method == "POST":
        fname = request.POST['fname']
        mail = request.POST['mail']
        subject = request.POST['subject']
        message = request.POST['message']

        # send an email to the institution
        send_mail(
            subject + ' ' + fname,  # subject,
            message,  # message,
            mail,  # from email,
            ['expertyomo62@gmail.com', ' expertprint02@gmail.com'],  # to email
        )

        return render(request, 'expt/contact.html', {'fname': fname})
    else:
        return render(request, 'expt/contact.html', {})


def testimonial(request):
    return render(request, 'expt/testimonial.html', {})


def terms(request):
    return render(request, 'expt/terms-and-conditions.html', {})
