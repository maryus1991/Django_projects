from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, get_user_model, authenticate, logout
from django.contrib.auth.models import User


# Create your views here.


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    login_form = LoginForm(request.POST or None)
    context = {
        'login_form': login_form
    }
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error('user_name', 'کاربری با مشخصات وارد شده یافت نشد')
            # login_form.add_error('password', 'رمز عبور شما اشتباه است')

    return render(request, 'login_auth.html', context)

    
def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    register_forms = RegisterForm(request.POST or None)
    context = {
        'register_forms':  register_forms
    }
    if register_forms.is_valid():
        user_name = register_forms.cleaned_data.get('user_name')
        email = register_forms.cleaned_data.get('email')
        password = register_forms.cleaned_data.get('password')
        User.objects.create_user(username=user_name, email=email, password=password)
        user_log = authenticate(request, username=user_name, password=password)
        if user_log is not None:
            login(request, user_log)
            return redirect('/')
        return redirect('/auth/login')

    return render(request, 'register_auth.html', context)


def logout_page(request):
    logout(request)
    return redirect('/')
