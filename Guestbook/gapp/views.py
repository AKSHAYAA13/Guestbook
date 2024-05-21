from django.shortcuts import render,redirect
from .forms import FeedbackForm
from .models import Feedback

# Create your views here.
def index(request):
    return render(request,'index.html')
def add(request):
    if request.method=="POST":
        form=FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('success')
    else:
        form=FeedbackForm()
    return render(request,'add.html',{'form':form})
def success(request):
    return render(request,'success.html')
def display(request):
    feeds=Feedback.objects.all()
    return render(request,'display.html',{'feeds':feeds})

