from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from user.forms import LoginForm
from django.contrib.auth.decorators import login_required


def user_login(request):
    ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
            else:
                form.add_error('Invalid Credentials!...')
    else:
        form = LoginForm()
    return render(request,'./user/login.html', {'form':form})


@login_required
def dashboard(request):
    ""
    return render(request, './user/dashboard.html')


def user_logout(request):
    ""
    logout(request)
    return redirect("login")