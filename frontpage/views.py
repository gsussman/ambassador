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
        print 'form is post'
        for key, values in request.POST.lists():
            print(key, values)
        name = form['name']
        highschool = form['hsInput']
        major = form['majorInput']
        activites = form['activitesInput']
        colleges = form.getlist('schoolInput')
        send_mail('Ambassador - New Signup', 'Here is the message.', 'info@findambassador.com', ['gene.sussman@gmail.com'], fail_silently=False)
        messages.success(request, 'Thank you for signing up! We will let you know when we offically launch!') 
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