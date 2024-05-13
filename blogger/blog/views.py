from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate


def index(request):
    return render(request, 'index.html')

def user_logout(request):
    logout(request)
    return redirect('index')