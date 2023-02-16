from django.shortcuts import render,redirect
from .forms import*
from .models import* 

# Create your views here.
def home(request):
    return render(request,'songreccom/home.html')

def Quiz(request):
    q=quiz.objects.all()
    context={'q':q}
    return render(request,'songreccom/quiz.html',context)
 
def addQuestion(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'Quiz/addQuestion.html',context)
    else: 
        return redirect('home') 