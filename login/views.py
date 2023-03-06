from django.shortcuts import render, redirect
from .forms import MyUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import User


# Create your views here.

def registerform(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        try:
            if form.is_valid:
                form.save()
                return redirect('login:login')
        except:
            messages.error(request, 'an error occurred during registration')
    else:
        form = MyUserCreationForm()
    return render(request, 'login/register.html', {'form': form})


def loginuser(request):
    if request.method == 'POST':
        # print(request.user)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('base:home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login/login.html')


def logoutuser(request):
    logout(request)
    return redirect('base:index')
