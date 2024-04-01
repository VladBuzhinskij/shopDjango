from django.shortcuts import render
from users.forms import UserLoginForm,UserRegistrationForm,ProfileForm
from django.contrib import auth,messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method=='POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user:
                auth.login(request,user)
                messages.success(request,"Вход выполнен")
                return HttpResponseRedirect(reverse('main:index'))  
    else:
        form=UserLoginForm()
    context={
        'title':'Авторизация',
        'form':form
    }
    return render(request, 'users/login.html', context)

@login_required
def registration(request):
    if request.method=='POST':
        form = UserRegistrationForm(data=request.POST)
        print('1')
        if form.is_valid():
            form.save()
            user=form.instance
            auth.login(request,user)
            messages.success(request,"Регистрация и вход выполнены")
            return HttpResponseRedirect(reverse('main:index'))  
    else:
        form=UserRegistrationForm()
    
    context={
        'title':'Авторизация',
        'form':form
    }
    return render(request, 'users/registration.html', context)

@login_required
def profile(request):
    if request.method=='POST':
        form = ProfileForm(data=request.POST, instance=request.user)
        print('1')
        if form.is_valid():
            form.save()
            messages.success(request,"Даные сохранены")
            return HttpResponseRedirect(reverse('user:profile'))  
    else:
        form=ProfileForm(instance=request.user)
    
    context={
        'title':'Профиль',
        'form':form
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    messages.success(request,"Выход выплонен")
    return HttpResponseRedirect(reverse('main:index'))