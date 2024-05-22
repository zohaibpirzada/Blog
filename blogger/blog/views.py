from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm
from .form import RegistrationForm, ProfilePicForm, ProfileUpdateForm, Add_blog, CategoryForm
from django.contrib.auth.models import User
from .models import Profile, Category

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
        username=request.POST['username']
        image_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=current_user_profile)
        form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=current_user)
        if image_form.is_valid() and form.is_valid():
            image_form.save()
            if username != '':
                form.save()
            else:
                messages.success(request, f"Put the Username!! ")
                print(request.META.get('HTTPS_REFERER'))
                return redirect('edit_profile')
            messages.success(request, f"{current_user.username}'s Profile Has Been Updated!!")
            return redirect('index')
    else:
        image_form = ProfilePicForm(instance=current_user_profile)
        form = ProfileUpdateForm(instance=current_user)
    return render(request, 'edit_profile.html', {'image_form': image_form, 'form' : form})

def add_blog(request):
    current_user = get_object_or_404(User, id=request.user.id)
    cat = Category.objects.all()
    if request.method == 'POST':
        form = Add_blog(request.POST or None, request.FILES or None)
        cat_form = CategoryForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post =form.save(commit=False)  
            post.user = request.user
            post.save()  
            messages.success(request, "your post successfuly added!!")
            return redirect('all_post')
        else:
            messages.success(request, "You miss the fill content!!")
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = Add_blog()
        cat_form = CategoryForm()
    return render(request, 'add_blog.html', {'form' : form, 'cat': cat, 'cat_form' : cat_form})

def Add_cat(request):
    if request.method == 'POST':
        cat_form = CategoryForm(request.POST or None, request.FILES or None)
        if cat_form.is_valid():
            post=cat_form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect(request.META.get('HTTP_REFERER'))
