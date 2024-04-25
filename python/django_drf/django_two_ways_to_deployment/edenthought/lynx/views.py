from django.shortcuts import render


def index(request):
    return render(request, 'lynx/index.html')


def dashboard(request):
    return render(request, 'lynx/dashboard.html')


def my_login(request):
    return render(request, 'lynx/my-loggin.html')


def register(request):
    return render(request, 'lynx/register.html')


def profile_management(request):
    return render(request, 'lynx/profile-management.html')


