from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.models import User


def index(request):
    return render(request, 'gear_manager/index.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'gear_manager/index.html')
        else:
            return render(request, 'gear_manager/login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'gear_manager/login.html')


def logout_user(request):
    logout(request)
    return render(request, 'gear_manager/index.html')


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmation_password = request.POST['confirmation_password']
        email_address = request.POST['email_address']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        if password != confirmation_password:
            return render(request, 'gear_manager/register.html', {'error_message': 'Passwords do not match'})

        try:
            user = User.objects.create_user(username=username, email=email_address, password=password, first_name=first_name, last_name=last_name)
            user.save()
        except IntegrityError:
            return render(request, 'gear_manager/register.html', {'error_message': 'Username already exists'})


        login(request, user)
        return render(request, 'gear_manager/index.html')

    return render(request, 'gear_manager/register.html')


def add_gear(request):
    return render(request, 'gear_manager/add_gear.html')
