from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        username = request.POST['username'] # because name=username on homepage (home.html)
        password = request.POST['password'] # because name=password on homepage (home.html)

        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is  not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "Error logging in!")
            return redirect('home')
    
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out succesfully...')
    return redirect('home')

