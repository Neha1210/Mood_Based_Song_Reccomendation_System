from django.shortcuts import render,redirect,reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from .forms import*
import random
from .models import* 

# Create your views here.

def home(request):
    return render(request,'songreccom/home.html')

def Quiz(request):
    items=list(quiz.objects.all())
    random.shuffle(items)
    q=items[:10]
    context={'q':q}
    return render(request,'songreccom/quiz.html',context)
        
def result(request):
    return render(request,'songreccom/result.html')

def about(request):
    return render(request,'songreccom/about.html')

def contact(request):
    return render(request,'songreccom/contact.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=CreateUserForm()
        if request.method=="POST":
            form=CreateUserForm(request.POST)
            if form.is_valid():
               form.save()
               user=form.cleaned_data.get('username')
               messages.success(request,"Account created successfully for"+" "+user)
               return redirect('login')
    

    context={'form':form}
    return render(request,'songreccom/register.html') 


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username='username',password='password')
        
            if user is not None:
               login(request,user)
               return redirect('home')
            else:
               messages.info(request,"username or password is incorrect")
    
    context={}
    return render(request,'songreccom/login.html')

def logout(request):
    logout(request)
    return redirect('login')
