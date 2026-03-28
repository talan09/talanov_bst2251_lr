from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput,
        min_length=8,
        error_messages={
            'min_length': 'Пароль должен быть не менее 8 символов'
        }
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        error_messages={
            'invalid': 'Введите корректный email адрес',
            'required': 'Email обязателен для заполнения'
        }
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        error_messages = {
            'username': {
                'required': 'Имя пользователя обязательно',
                'unique': 'Пользователь с таким именем уже существует'
            }
        }


    def clean_username(self):
        username = self.cleaned_data.get('username')


        if not username:
            raise ValidationError('Имя пользователя не может быть пустым')


        if User.objects.filter(username=username).exists():
            raise ValidationError('Пользователь с таким именем уже существует')

        return username


    def clean_email(self):
        email = self.cleaned_data.get('email')


        if not email:
            raise ValidationError('Email не может быть пустым')


        if User.objects.filter(email=email).exists():
            raise ValidationError('Пользователь с таким email уже существует')

        return email


    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')


        if not password1:
            self.add_error('password1', 'Пароль не может быть пустым')

        if not password2:
            self.add_error('password2', 'Подтверждение пароля не может быть пустым')


        if password1 and password2 and password1 != password2:
            raise ValidationError('Пароли не совпадают')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])  # Хешируем пароль
        if commit:
            user.save()
        return user