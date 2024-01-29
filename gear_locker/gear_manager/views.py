from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import GearListItem, Category


def index(request):
    return render(request, 'gear_manager/index.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'gear_manager/login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'gear_manager/login.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


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

    return HttpResponseRedirect(reverse('index'))


@login_required(login_url='login')
def add_gear(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        weight = request.POST['weight']
        url = request.POST['url']
        image = request.POST['image']
        category = request.POST['category']

        if price == '':
            price = 0
        else:
            price = float(price)

        if weight == '':
            weight = 0
        else:
            weight = float(weight)

        try:
            cat = Category.objects.get(name=category)
        except Category.DoesNotExist:
            cat = Category.objects.create(name=category, description=category, entered_by=request.user)

        new_item = GearListItem.objects.create(name=name, description=description, price=price, weight=weight, url=url, image=image, entered_by=request.user, category=cat)
        new_item.save()

        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'gear_manager/add_gear.html')
