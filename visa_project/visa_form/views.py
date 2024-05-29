from django.shortcuts import render, redirect
from .models import VisaApplication
from .forms import VisaApplicationForm


# Create your views here.

def visa_appliation(request):
    if request.method == "POST":
        form = VisaApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')

    else:
        form = VisaApplicationForm()
    return render(request, 'visa_form/application.html',{'form':form})

def success(request):
    return render(request, 'visa_form/success.html')

