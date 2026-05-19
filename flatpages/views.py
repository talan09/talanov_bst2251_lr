from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from lab3.articles.models import Article
from django.contrib.auth import login
from django.http import Http404
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == "POST":
        # Получаем данные из формы
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()
        password_confirm = request.POST.get("password_confirm", "").strip()
        
        # Словарь для ошибок
        errors = {}
        
        # Проверка на пустые поля
        if not username:
            errors['username'] = "Имя пользователя не может быть пустым"
        if not email:
            errors['email'] = "Email не может быть пустым"
        if not password:
            errors['password'] = "Пароль не может быть пустым"
        if not password_confirm:
            errors['password_confirm'] = "Подтверждение пароля не может быть пустым"
        
        if username and User.objects.filter(username=username).exists():
            errors['username'] = "Пользователь с таким именем уже существует"
        
        if email and User.objects.filter(email=email).exists():
            errors['email'] = "Пользователь с таким email уже существует"
        
        if password and password_confirm and password != password_confirm:
            errors['password_confirm'] = "Пароли не совпадают"
        
        if password and len(password) < 6:
            errors['password'] = "Пароль должен содержать минимум 6 символов"
        
        if not errors:
            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                login(request, user)
                return redirect('flatpages:archive')  
            except Exception as e:
                errors['general'] = "Произошла ошибка при регистрации. Пожалуйста, попробуйте позже."
        
        return render(request, 'register.html', {
            'errors': errors,
            'username': username,
            'email': email
        })
    
    # GET запрос - показываем пустую форму
    return render(request, 'register.html')
def home(request):
    return render(request, 'welcome.html', {"posts": Article.objects.all()})
def helloWold(request):
    return HttpResponse('Привет мир!')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('flatpages:archive')
        else:
            return render(request, 'login.html', {'error': 'Неверное имя пользователя или пароль'})
    return render(request, 'login.html')

def js(request):
    return render(request, 'static_handler.html');