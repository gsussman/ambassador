from django.shortcuts import render
from signup.forms import EmailSignupForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from frontpage.forms import SignupForm
from django.core.mail import send_mail

# Create your views here.

def home(request):

    if request.method == "POST":
        form = EmailSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for signing up! We will let you know when we offically launch!') 
        return HttpResponseRedirect('/')
    else:
    	form = EmailSignupForm()
    	return render(request, 'frontpage/home.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = request.POST
        for key, values in request.POST.lists():
            print(key, values)
        name = form['name']
        email = form['emailInput']
        highschool = form['hsInput']
        major = form['majorInput']
        activities = form['activitiesInput']
        colleges = form.getlist('schoolInput')
        message = 'New Signup\nName - {name}\nEmail - {email}\nHigh School - {highschool}\nMajor - {major}\nActivities - {activities}\nColleges - {colleges}\n\nKeep Being Awesome'.format(name=name, email=email, highschool=highschool, major=major, activities=activities, colleges=colleges)
        send_mail('Ambassador - New Signup', 'Name message', 'info@findambassador.com', ['gene.sussman@gmail.com'], fail_silently=False)
        messages.success(request, 'Thank you for signing up! We will be in touch with you shortly.') 
        return HttpResponseRedirect('/signup/')
    else:
    	form = EmailSignupForm()
    	return render(request, 'frontpage/signup.html', {'form': form})

def hiw(request):

    if request.method == "POST":
        form = EmailSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for signing up! We will let you know when we offically launch!') 
        return HttpResponseRedirect('/')
    else:
        form = EmailSignupForm()
        return render(request, 'frontpage/hiw.html', {'form': form})