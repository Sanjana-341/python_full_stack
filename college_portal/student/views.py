from django.shortcuts import render
from django.http import HttpResponse
from .models import Student_table
from .form import Student_form_data
# Create your views here.
def home(request):
    data={
        'name':"Sanaju",
        'age':17,
        'department':"BCA"
    }
    marks=[90,45,60]
    return render(request,'home.html',{'data':data,'marks':marks})
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def forms(request):
    if request.method=="POST":
        reg_no=request.POST.get('reg_no')
        name=request.POST.get('name')
        email=request.POST.get('email')
        marks=request.POST.get('marks')
        dob=request.POST.get('dob')
        Student_table.objects.create(reg_no=reg_no,name=name,email=email,marks=marks,dob=dob)
        return HttpResponse("saved successfully")
    return render(request,'Student_form.html')
def Student_form_dj(request):
    if request.method=="POST":
        form=Student_form_data(request.POST)
        if form.is_valid():
            reg_no1=form.cleaned_data['reg_no1']
            name1=form.cleaned_data['name1']
            email1=form.cleaned_data['email1']
            return HttpResponse("Saved Successfully!")
        else:
            return HttpResponse("Invalid Data")
    else:
        form=Student_form_data()
        return render(request,'Student_form_data.html',{'form':form})
