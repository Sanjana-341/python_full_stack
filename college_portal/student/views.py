from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student_table
from .form import Student_form_data
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
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
def user_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid Username or Password")
    return render(request,'login.html')
@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html')

from django.contrib.auth import logout
from django.http import HttpResponse


from django.contrib.auth import logout
from django.http import HttpResponse

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponse("""
            <html>
            <head>
                <title>Logout Successful</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background: linear-gradient(135deg, #667eea, #764ba2);
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                    }

                    .container {
                        background: white;
                        padding: 40px;
                        border-radius: 15px;
                        text-align: center;
                        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
                    }

                    h2 {
                        color: #28a745;
                    }

                    p {
                        color: #555;
                        font-size: 16px;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h2>✓ Logout Successful!</h2>
                    <p>You have logged out successfully.</p>
                </div>
            </body>
            </html>
        """)

    return HttpResponse("""
        <html>
        <body style="background:#fff0f0; text-align:center; padding:100px;">
            <h2 style="color:red;">⚠ Invalid Request!</h2>
            <p>Please try again.</p>
        </body>
        </html>
    """)
