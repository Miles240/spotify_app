from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        # check if user is availble in the database
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'login.html')


def signup(request):
    # Collect user data
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        
        if password == password2:
            # Check if user already exist 
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            else: # Create a new user if it dosen't exist
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()

                # Log user in
                user_login = auth.authenticate(
                    username=username, password=password)
                auth.login(request, user_login)
                return redirect('/')

        else:
            messages.info(request, 'Input Matching Passwords')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')
