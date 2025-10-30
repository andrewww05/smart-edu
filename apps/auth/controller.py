from django.http import request
from django.shortcuts import render, redirect
from apps.auth.service import AuthService
from apps.auth.forms import RegisterForm, LoginForm

class AuthController:
    _authService = AuthService()

    def login(self, request: request):
        if request.method == "GET":
            return render(request, 'page/auth/login.html', {})
        
        elif request.method == 'POST':
            form = LoginForm(request.POST)

            if form.is_valid():
                data = form.cleaned_data
                
                # TODO: Implemnt auth
                if data.get('remember'):
                    request.session.set_expiry(60 * 60 * 24 * 30)
                else:
                    request.session.set_expiry(0)

                return redirect('login')
            else:
                return render(request, 'page/auth/login.html', {'form': form})
    
    def register(self, request: request):
        if request.method == "GET":
            return render(request, 'page/auth/register.html', {})
        
        elif request.method == 'POST':
            form = RegisterForm(request.POST)

            if form.is_valid():
                data = form.cleaned_data

                # User.objects.create_user(
                #     email=data['email'],
                #     password=data['password'],
                #     first_name=data['first_name'],
                #     second_name=data['second_name']
                # )

                if data.get('remember'):
                    request.session.set_expiry(60 * 60 * 24 * 30)
                else:
                    request.session.set_expiry(0)

                return redirect('login')
            else:
                return render(request, 'page/auth/register.html', {'form': form})
            
    def verify_email(self):
        # TODO: Verify email
        pass