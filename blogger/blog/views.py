from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm
from .form import RegistrationForm

def index(request):
    return render(request, 'index.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'User was succesfully logout')
    return redirect('index')
def user_login(request):
    if request.user.is_authenticated:
        messages.success(request, 'You are already logged!')
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user != None:
                login(request, user)
                messages.success(request, f'{request.user.username} are succesfully login')
                return redirect('index')
            else:
                messages.success(request, f'User Not Found')

        return render(request, 'login.html')

def user_sign(request):
    if request.user.is_authenticated:
        messages.success(request, 'You are already logged!')
        return redirect('index')
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST or None)
            if form.is_valid():
                form.save()
                username = request.POST['username']
                password = request.POST['password1']
                new_user = authenticate(username=username, password=password)
                if new_user != None:
                    login(request, new_user)
                    return redirect('index')
        else:
            form = RegistrationForm()
        return render(request, 'sigin.html', {'form': form})