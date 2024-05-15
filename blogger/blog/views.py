from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm
from .form import RegistrationForm, ProfilePicForm, ProfileUpdateForm
from django.contrib.auth.models import User
from .models import Profile

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
    
def edit_profile(request):
    current_user = get_object_or_404(User, id=request.user.id)
    current_user_profile = get_object_or_404(Profile, user__id=request.user.id)
    if request.method == 'POST':
        image_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=current_user_profile)
        form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=current_user)
        if image_form.is_valid() and form.is_valid():
            image_form.save()
            form.save()
            messages.success(request, f"{current_user.username}'s Profile Has Been Updated!!")
            return redirect('index')
    else:
        image_form = ProfilePicForm(instance=current_user_profile)
        form = ProfileUpdateForm(instance=current_user)
    return render(request, 'edit_profile.html', {'image_form': image_form, 'form' : form})