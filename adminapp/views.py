from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pyexpat.errors import messages

from .models import Admin,Student,Faculty,Course
# Create your views here.
def adminhome(request):
    return render(request,'adminhome.html')

def logout(request):
    return render(request,'login.html')

def signup1(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Oops! Username Already Taken.')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, email=email, password=pass1,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                messages.info(request, 'Account created successfully')
                user_details = {
                    'username': username,
                    'email': email,
                    'first_name': first_name,
                    'last_name': last_name
                }
                return render(request, 'ProjectHomePage.html',
                              {'user_details': user_details})  # Redirect to account details page
        else:
            messages.info(request, 'Password does not match')
            return render(request, 'signup.html')

    return render(request, 'signup.html')


# def login(request):
#     return render(request, 'login.html')
#
#
# def login1(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         pass1 = request.POST['password']
#         user = auth.authenticate(username=username, password=pass1)
#         if user is not None:
#             auth.login(request, user)
#             if len(username) == 10:
#                 return redirect('EventParticipantHomePage')
#
#         else:
#             messages.info(request, 'Invalid Credentials')
#             return render(request, 'login.html')
#     else:
#         return render(request, 'login.html')

def checkadminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)

            return redirect('adminhome')

        else:
            # return HttpResponse("Invalid request method.")
            return render(request, 'adminhome.html')
    else:
        return render(request, 'login.html')
def viewstudents(request):
    students=Student.objects.all()
    count = Student.objects.count()
    return render(request,"viewstudents.html",{"studentdata":students,"count":count})

def viewfaculty(request):
    faculty=Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request,"viewfaculty.html",{"facultydata":faculty,"count":count})

def viewcourses(request):
    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request,"viewcourses.html",{"coursedata":courses,"count":count})

def adminfaculty(request):
    return render(request,'adminfaculty.html')

def admincourse(request):
    return render(request,'admincourse.html')

def adminstudent(request):
    return render(request,'adminstudent.html')

def success(request):
    return render(request,'success.html')

