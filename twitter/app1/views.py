from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from app1.models import tweet
# Create your views here.
def homeview(request):
    objs=tweet.objects.all()[::-1]
    return render(request,'home.html',{'result':objs})

def loginview(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method=="POST":
        username=request.POST.get('usern')
        password=request.POST.get('pswd')
        print(username,password)
        result=authenticate(request,username=username,password=password)
        if result is not None:
            login(request,result)
            if request.user.is_superuser:
                return redirect('/admin')
            else:
                return redirect('profilepage')
    return render(request,'login.html')


def registerview(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        uname=request.POST.get('uname')
        email=request.POST.get('mail')
        pwd=request.POST.get('pwd')
        cpwd=request.POST.get('cpwd')
        if User.objects.filter(username=uname).exists():
            return redirect('loginpage')
        if len(pwd)<8:
            return redirect('registerpage')
        if (pwd!=cpwd):
            return redirect('registerpage')
        obj=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pwd)
        obj.save()
        return redirect('loginpage')
    return render(request,'register.html')

@login_required(login_url='loginpage')
def profileview(request):
    if request.user.is_superuser:
        return redirect('/admin')
    else:
        return render(request,'profile.html')

@login_required(login_url='loginpage')
def createview(request):
    if request.method=="POST":
        a=request.POST.get('post')
        uname=str(request.user.username)
        obj=tweet(username=uname,post=a)
        obj.save()
        return redirect('homepage')
    return render(request,'create.html')

def logoutview(request):
    logout(request)
    return redirect('loginpage')

def deleteview(request,rid):
    if request.user.is_superuser:
        obj=tweet.objects.get(id=rid)
        obj.delete()
        return redirect('homepage')
    return render(request,'home.html')

def singleview(request,rid):
    b=tweet.objects.get(id=rid)
    if request.method=="POST":
        b.post=request.get(id=rid)
        b.save()
    return redirect(request,'home.html')