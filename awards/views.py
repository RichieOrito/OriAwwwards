from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'index.html',)

def register_user(request):
    return render(request, 'auth/register.html',)

def login_user(request):
    return render(request, 'auth/login.html',)

def log_out(request):
    logout(request)
    return redirect('login')

def profile(request):
    return render(request, 'profile.html',)