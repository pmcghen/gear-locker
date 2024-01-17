from django.shortcuts import render


def index(request):
    return render(request, 'gear_manager/index.html')
