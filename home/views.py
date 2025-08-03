from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout as core_logout
from django.contrib.auth import authenticate, login
from . models import profile , courseOffer , interviewOffer , jobOffer


def index(request):
    return render(request, "index.html")


def loginn(request):
    if request.user.is_authenticated:
        core_logout(request)
        
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            loggedprofile = profile.objects.get(user=request.user)
            if loggedprofile.account_type == "candidate":
                return render(request, "candidatelogin.html",{'loggedprofile':loggedprofile})
            elif loggedprofile.account_type == "company":
                return render(request, "companylogin.html",{'loggedprofile':loggedprofile})
            else:
                return render(request,'login.html')
    return render(request,'login.html')

def logout(request):
     core_logout(request)
     return redirect('loginn')
    


def signup(request):
    if request.user.is_authenticated:
        core_logout(request)
        
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        accounttype = request.POST["accounttype"]
        phonenumber = request.POST["phone"]
        birthday = request.POST["birth_date"]
        profilephoto = request.FILES["profilephoto"]
        myuser = User.objects.create_user(username, email, password)
        myprofile = profile(user=username,account_type=accounttype,phone_number=phonenumber,birth_date=birthday,profile_picture=profilephoto)
        if request.POST["accounttype"] == "candidate":
            myuser.save()
            myprofile.save()
            return redirect('loginn')
        elif request.POST["accounttype"] == "company":
            myuser.save()
            myprofile.save()
            return redirect('loginn')
        else:
            return render(request, "signup.html")
    return render(request, "signup.html")

def addcourse(request):
    if request.user.is_authenticated:
        loggedprofile = profile.objects.get(user=request.user)
        if request.method == "POST":
            username = request.user
            about = request.POST["about"]
            coursefee = request.POST["coursefee"]
            phonenumber = request.POST["phonenumber"]
            link = request.POST["link"]
            postingphoto = request.FILES["postingphoto"]
            name = request.POST["name"]
            course = courseOffer(user=username,name=name,about=about,course_fee=coursefee,phone_number=phonenumber,posting_photo=postingphoto,link=link)
            course.save()
            return render(request, "companylogin.html",{'loggedprofile':loggedprofile})
        return render(request, "addcourse.html",{'loggedprofile':loggedprofile})
    else:
        return redirect('loginn')
    

def addinterview(request):
    if request.user.is_authenticated:
        loggedprofile = profile.objects.get(user=request.user)
        if request.method == "POST" :
            username = request.user
            about = request.POST["about"]
            phonenumber = request.POST["phonenumber"]
            link = request.POST["link"]
            postingphoto = request.FILES["postingphoto"]
            name = request.POST["name"]
            interview = interviewOffer(user=username,name=name,about=about,phone_number=phonenumber,posting_photo=postingphoto,link=link)
            interview.save()
            return render(request, "companylogin.html",{'loggedprofile':loggedprofile})
        return render(request, "addinterview.html",{'loggedprofile':loggedprofile})
    else:
        return redirect('loginn')

def addjob(request):
    if request.user.is_authenticated:
        loggedprofile = profile.objects.get(user=request.user)
        if request.method == "POST":
            username = request.user
            about = request.POST["about"]
            phonenumber = request.POST["phonenumber"]
            jobsalary = request.POST["jobsalary"]
            link = request.POST["link"]
            postingphoto = request.FILES["postingphoto"]
            name = request.POST["name"]
            job = jobOffer(user=username,name=name,about=about,job_salary=jobsalary,phone_number=phonenumber,posting_photo=postingphoto,link=link)
            job.save()
            return render(request, "companylogin.html",{'loggedprofile':loggedprofile})
        return render(request, "addjob.html",{'loggedprofile':loggedprofile})
    else:
        return redirect('loginn')

def showcourse(request):
    if request.user.is_authenticated:
        courses = courseOffer.objects.all()
        loggedprofile = profile.objects.get(user=request.user)
        return render(request,'showcourses.html',{'courses':courses,'loggedprofile':loggedprofile})
    else:
        return redirect('loginn')

def showjob(request):
    if request.user.is_authenticated:
        jobs = jobOffer.objects.all()
        loggedprofile = profile.objects.get(user=request.user)
        return render(request,'showjobs.html',{'jobs':jobs,'loggedprofile':loggedprofile})
    else:
        return redirect('loginn')

def showinterview(request):
    if request.user.is_authenticated:
        interviews = interviewOffer.objects.all()
        loggedprofile = profile.objects.get(user=request.user)
        return render(request,'showinterviews.html',{'interviews':interviews,'loggedprofile':loggedprofile})
    else:
        return redirect('loginn')
# Create your views here.
