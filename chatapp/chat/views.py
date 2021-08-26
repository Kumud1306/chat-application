from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def chat(request):
    
    return render(request,'chat.html',{})

def signup(request):
    if request.user.is_authenticated:
        return redirect("chat")
    else:
        if request.method== 'POST':
            username = request.POST['username']
            password1 = request.POST['password']
            email = request.POST['email']
            user = User.objects.create_user(username=username,email=email,password=password1)
            if user:
                return redirect("login")
    return render(request,'signup.html',{})

def Login(request):
    if request.user.is_authenticated:
        return redirect("chat")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            if username and password:
                user = authenticate(username=username,password=password)
                if user:
                    login(request,user)
                    return redirect("chat")
    return render(request,'login.html',{})
def Logout(request):
    logout(request)
    return redirect("chat")