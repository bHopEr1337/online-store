from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.models import User
from users.forms import UserLoginForm, UserRegistartionForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form' : form}
    return render(request, template_name='users/login.html', context=context)


def register(request):
    if request.method == "POST":
        form = UserRegistartionForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
            form = UserRegistartionForm()
    context = {'form' : form}
    return render(request, 'users/register.html', context)

    form = UserRegistartionForm()
    context = {'form' : form}
    return render(request, template_name='users/register.html', context=context)