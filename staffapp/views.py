from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import registeration,Userform,Profileform
from django.contrib.auth.decorators import login_required
from .import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages

def home_view(request):
    return render(request,'home.html',{})


def search_detial(request):
    query=request.GET.get('q')
    lookups=Q(first_name__icontains=query) | Q(last_name__icontains=query)
    objects=User.objects.filter(lookups)
    
    return render (request,"detial_view.html",{"object":objects})

def login_view(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            context={"error":"invaild username or password"}
            return render(request,'login.html',context=context)
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    messages.success(request,"logged out successfully")
    return redirect('home')

def sigup_views(request):
    if request.method=="POST":
        form=registeration(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')
    else:
        form =registeration()
    return render(request,'signup.html',{"form":form})


def profile_view2(request,id):
    profile=models.Profile.objects.get(user=id)
    return render (request,'profile.html',{"profile":profile})

@login_required(login_url='login')
def profile_view(request):
    profile=models.Profile.objects.get(user=request.user)
    return render (request,'profile.html',{"profile":profile})

@login_required(login_url='login')
def profile_edit(request):
    profile = models.Profile.objects.get(user=request.user)

    if request.method=='POST':
        userform = Userform(request.POST,instance=request.user)
        profileform = Profileform(request.POST,request.FILES,instance=profile )
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect('profile')

    else :
        userform = Userform(instance=request.user)
        profileform = Profileform(instance=profile)

    context={'userform':userform , 'profileform':profileform,"profile":profile}
    return render(request,'profile_edit.html',context=context)

