from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from datetime import datetime
from shop.models import Contact
from django.contrib import messages

# password for test user is:
# dv5!5nl87%

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def products(request):
    return render(request,'products.html')

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        contact = Contact(fname=fname,lname=lname,email=email,phone=phone,subject=subject,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')

    return render(request,'contact.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request,'login.html')
            
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")


    