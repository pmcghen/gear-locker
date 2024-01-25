from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

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



def add_gear(request):
    return render(request, 'gear_manager/add_gear.html')
