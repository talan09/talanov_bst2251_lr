from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User



def register(request):
    if request.method == 'POST':

        user = User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password1'),
            email=request.POST.get('email')
        )

        login(request, user)
        messages.success(request, 'Регистрация прошла успешно!')
        return redirect('articles:archive')

    return render(request, 'registration.html')



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username is not None and password is not None:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {username}!')
                return redirect('/articles')
            else:
                messages.error(request, 'Неверное имя пользователя или пароль')
                return redirect(request.path)
        else:
            messages.error(request, 'Обязательно для заполнения')
            return redirect(request.path)
    return render(request, 'login.html')



def logout_user(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы')
    return redirect('articles:archive')