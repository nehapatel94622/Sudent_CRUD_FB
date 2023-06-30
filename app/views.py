from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.
#This function is add data and showdata
def show_data(request):
    if request.method == 'POST':
     fm = StudentRegistration(request.POST)
     if fm.is_valid():
        fm.save()
        fm = StudentRegistration()
    
    else:
        fm = StudentRegistration()
    data = User.objects.all()
    return render(request, 'show_data.html', {'form':fm, 'stu':data})

#This function will delete
def del_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return redirect('showdata')

#this fuction will edit data
def edit_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    
    return render(request, 'update.html', {'form':fm})



