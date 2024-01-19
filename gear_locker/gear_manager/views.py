from django.shortcuts import render


def index(request):
    return render(request, 'gear_manager/index.html')


def add_gear(request):
    return render(request, 'gear_manager/add_gear.html')
