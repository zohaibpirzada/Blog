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
    if request.method == 'GET':
        select = request.GET.get('filter')
        if select == 'All':
            categories = Category.objects.order_by('-create_date')
        elif select != None:
            categories = Category.objects.filter(user__username=select).order_by('-create_date')
            print(select)
        # elif select == '':
    return render(request, 'all_categories.html', {'categories' : categories})

def delete_cat(request, cat_id):
    category = get_object_or_404(Category, id=cat_id)
    if request.user.id == category.user.id or request.user.id == 1:
        category.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.success(request,'That is not you category')
        return redirect('all_categories')
        # return redirect(request.META.get('HTTP_REFERER'))