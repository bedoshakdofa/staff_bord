from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import registeration,Userform,Profileform
from django.contrib.auth.decorators import login_required
from .import models
from django.contrib.auth.models import User

def home (request):
    return render(request,'home.html')

def search_detial(request):
    if request.method=="POST":
        print("test1")
        q=request.POST.get('q')
        data=User.objects.filter(first_name__icontains=q)
    context={"data":data}

    return render (request,'detial_view.html',context)
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
    if request.method=="POST":
        logout(request)
        return redirect('home')
    return render(request,'logout.html')

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








# def profile_edit(request):
#     active_user= models.Profile.objects.get(user=request.user)
#     print("test0")
#     if request.method=='POST':
#         print("test1")
#         userform=Userform(request.POST,instance=request.user)
#         profileform=Profileform(request.POST,request.FILES,instance=active_user)
#         if userform.is_valid() and profileform.is_valid():
#             print('test2')
#             userform.save()
#             myprofile = profileform.save(commit=False)
#             myprofile.user = request.user
#             myprofile.save()
#             return redirect('profile')
#     else:
#         print("test3")
#         userform=Userform(instance=request.user)
#         profileform=Profileform(instance=active_user)
#     return render (request,'profile_edit.html',{"userfrom":userform , "profileform":profileform})