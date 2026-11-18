from django.shortcuts import render
from django.http import HttpResponse
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