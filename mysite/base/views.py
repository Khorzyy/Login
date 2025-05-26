from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import Register, LoginForm

def register_view(request):
    if request.method == 'POST': 
        form = Register(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = Register()
    return render(request, 'base/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.cleaned_data['user']) 
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'base/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
