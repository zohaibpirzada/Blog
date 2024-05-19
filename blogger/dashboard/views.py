from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from django.contrib.auth.models import User
from blog.models import Profile, Category, Blog
from .form import CategoryForm


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
        all_post = Blog.objects.order_by('-pub_date')
        return render(request, 'all_post.html', {"all_post" : all_post})
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
    user = get_object_or_404(User, id=request.user.id)
    profile = get_object_or_404(Profile, user=user)
    if profile.staff == 'Approved':
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
    else:
        messages.success(request, 'Your are not team staff')
        return redirect('index')
    

def delete_cat(request, cat_id):
    category = get_object_or_404(Category, id=cat_id)
    if request.user.id == category.user.id or request.user.id == 1:
        category.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.success(request,'That is not you category')
        return redirect('all_categories')
        # return redirect(request.META.get('HTTP_REFERER'))

def add_category(request):
    log_user = get_object_or_404(User, id=request.user.id)
    profile = get_object_or_404(Profile, user=log_user)
    if profile.staff == 'Approved':
        user = User.objects.exclude(id=request.user.id).all()
        if request.method == 'POST':
            cat_user = request.POST.get('cat_user')
            form = CategoryForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                post = form.save(commit=False)
                post.user_id = cat_user
                post.save()
                return redirect('all_categories')
        else:
            form = CategoryForm()
        return render(request, 'add_category.html', {'users' : user, 'form' : form})
    else:
        messages.success(request, 'Your are not team staff')
        return redirect('index')

