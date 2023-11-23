from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from expert.models import Appointment, Contact, Enquiry


# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST['gname']
        gmail = request.POST['gmail']
        cname = request.POST['cname']
        vehicle = request.POST['vehicle']
        message = request.POST['message']

        data = Enquiry(name=name, gmail=gmail, courses=cname, vehicleclass=vehicle, message=message)
        data.save()

        # send email
        send_mail(
            cname + ' ' + name,  # subject,
            message + vehicle,  # message,
            gmail,  # from email,
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
    if request.method == "POST":
        aname = request.POST['aname']
        email = request.POST['gemail']
        date = request.POST['date']
        time = request.POST['time']
        phone = request.POST['phone']
        location = request.POST['location']
        message = request.POST['message']

        data = Appointment(name=aname, email=email,date=date, time=time, pnumber=phone, location=location, message=message)
        data.save()

        subject = 'Booking Appointment for' + '  ' + aname

        # send an email to the institution
        send_mail(
            subject,  # subject,
            message + ' ' + phone + 'from' + location + '. booking an appointment for ' + date + time,  # message,
            email,  # from email,
            ['plpgroup25@gmail.com', 'expertyomo62@gmail.com', ' expertprint02@gmail.com'],  # to email
        )
        if send_mail == 1:
            return HttpResponse(messages.success('Your email was sent successfully'))
        else:
            pass
            # return render(request, 'expt/404.html', {})

        return render(request, 'expt/appointment.html', {
            'name': aname,
            'email': email,
            'phone': phone,
            'date': date,
            'time': time,
            'location': location,
            'message': message,
        })
    else:
        return render(request, 'expt/appointment.html', {})


def error(request):
    return render(request, 'expt/404.html', {})


def contact(request):
    if request.method == "POST":
        fname = request.POST['fname']
        email = request.POST['mail']
        subject = request.POST['subject']
        message = request.POST['message']

        data = Contact(name=fname, subject=subject, message=message)
        data.save()

        # send an email to the institution
        send_mail(
            subject + ' ' + fname,  # subject,
            message,  # message,
            email,  # from email,
            ['plpgroup25@gmail.com', 'expertyomo62@gmail.com', ' expertprint02@gmail.com'],  # to email
        )

        return render(request, 'expt/contact.html', {'fname': fname})
    else:
        return render(request, 'expt/contact.html', {})


def testimonial(request):
    return render(request, 'expt/testimonial.html', {})


def terms(request):
    return render(request, 'expt/terms-and-conditions.html', {})
