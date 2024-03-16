from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.cache import never_cache


# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    print('home')
    return render(request,'home1.html')
    
    
@never_cache
def LoginPage(request):
    if request.user.is_authenticated:
        print('returned')
        return redirect('home')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"INVALID USERNAME AND PASSWORD")
            return redirect('login')
    return render (request,'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')   

