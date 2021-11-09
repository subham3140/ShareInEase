from django.shortcuts import redirect, render
from .models import User, FileModel
from django.contrib.auth import login, authenticate, logout


def login_user(request):
    if request.method == 'POST':
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(email=email, password=password)
            print(email, password, user)
            if user:
              login(request, user)  
              return redirect('home')
    return redirect("register")

def logout_user(request):
    logout(request)
    return redirect("login")
