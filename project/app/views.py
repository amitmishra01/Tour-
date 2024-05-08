from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm,PasswordChangeForm
from django.contrib import messages


# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout




def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirm_password')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not same")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            messages.success(request,"Account created successfully!!")
            return HttpResponseRedirect('/login/')


    return render (request,'tourest-master/signup.html')



def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            username=request.POST.get('username')
            pass1=request.POST.get('password')
            user=authenticate(request,username=username,password=pass1)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse("username or password is incorrect!!!")

        
        return render(request,'tourest-master/login.html')

    else:
         return HttpResponseRedirect('/home')


def home(request):
    if (request).user.is_authenticated:
        return render(request,'tourest-master/home.html')

    else:
        return HttpResponseRedirect('/login')


def contact(request):
    if (request).user.is_authenticated:
        return render(request,'tourest-master/contact.html')

    else:
        return HttpResponseRedirect('/home')


def about(request):
    if (request).user.is_authenticated:
        return render(request,'tourest-master/about.html')

    else:
        return HttpResponseRedirect('/home')   



def blog(request):
    if (request).user.is_authenticated:
        return render(request,'tourest-master/blog.html')

    else:
        return HttpResponseRedirect('/home')   

def tour(request):
    if (request).user.is_authenticated:
        return render(request,'tourest-master/tour.html')

    else:
        return HttpResponseRedirect('/home') 


def Destinations(request):
    if (request).user.is_authenticated:
        return render(request,'tourest-master/Destinations.html')

    else:
        return HttpResponseRedirect('/home')  

    
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login')




'''def forget_password(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm = SetPasswordForm(user = request.user,data = request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'password changed successfully')
                return HttpResponseRedirect('/home/')
        else:
            fm=SetPasswordForm(user=request.user)
        return render(request,'tourest-master/changepass.html',{'from':fm})
    else:
        return HttpResponseRedirect('/login')'''
