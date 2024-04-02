from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
from .forms import AddRecordForm

# Create your views here.

def home(request):

    records = Record.objects.all()
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
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out succesfully...')
    return redirect('home')

def view_record(request, pk):
    if request.user.is_authenticated:

        # look for record
        view_record = Record.objects.get(id=pk)
        return render(request, 'view_record.html', {'view_record': view_record})
    else:
        messages.success(request, 'You must be logged in to view this page...')
        return render(request, 'home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
            
        return render(request, 'add_record.html', {'form':form})
    
    else:
        messages.success(request, 'You must be logged in to view this page...')
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:

        # Get current record
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, 'Record deleted successfully...')
        return redirect('home')
    else:
        messages.success(request, 'You must be logged in to view this page...')
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        
        # get current record
        update_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=update_record) 
        # instance will propogate the AddRecordForm with existing values from the database
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Record has been updated!')
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    
    else:
        messages.success(request, 'You must be logged in to view this page...')
        return redirect('home')
