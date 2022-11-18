from django.shortcuts import render, HttpResponse, redirect

from courses.models import Course


def home(request):
    return render(request, 'home.html', )


def aboutUs(request):
    return render(request, 'about.html', {})


def Contactus(request):
    return render(request, 'contact.html', {})
