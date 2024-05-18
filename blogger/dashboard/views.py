from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from django.contrib.auth.models import User
from blog.models import Profile, Category

def dashboard(request):
    user = get_object_or_404(User, id=request.user.id)
    profile = get_object_or_404(Profile, user=user)
    if profile.staff == 'Approved':
        return render(request, 'dashboard.html')
    else:
        messages.success(request, 'Your are not team staff')
        return redirect("index")
    
def all_post(request):
    user = get_object_or_404(User, id=request.user.id)
    profile = get_object_or_404(Profile, user=user)
    if profile.staff == 'Approved':
        return render(request, 'all_post.html')
    else:
        messages.success(request, 'Your are not team staff')
        return redirect('index')
def my_post(request):
    user = get_object_or_404(User, id=request.user.id)
    profile = get_object_or_404(Profile, user=user)
    if profile.staff == 'Approved':
        return render(request, 'my_post.html')
    else:
        messages.success(request, 'Your are not team staff')
        return redirect('index')
    
def all_categories(request):
    categories = Category.objects.order_by('-create_date')
    return render(request, 'all_categories.html', {'categories' : categories})