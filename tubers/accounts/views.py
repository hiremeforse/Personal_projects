from django.shortcuts import redirect, render

from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth



# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            messages.error(request,'logged in')
            return redirect('dashboard')
            print("in_this")

        else:
            messages.error(request,'invalid crediatinals')
            return redirect('login')
            print("in_Ssecond")


    return render (request, 'accounts/login.html' )


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password']

        if password == confirm_password:
           if User.objects.filter(username=username).exists():
               messages.error(request , 'user_exists')
               return (request, 'login')
           else:
               if User.objects.filter(email=email).exists():
                   messages.error(request , 'email_exists')
               else:
                   user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                   user.save()
                   messages.success(request, 'acount created successfully')
                   return redirect('login')
        else:
            messages.error(request, 'password do not match')
            return redirect('register')

    return render (request, 'accounts/register.html' )

def logout_user(request):
    logout(request)
    return redirect('home') 

def dashboard(request):
    return render (request, 'accounts/dashboard.html' )