from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from apps.auth.forms import RegisterForm, LoginForm
from apps.auth.decorators import unauthorized_only, authorized_only

class AuthController:
    @unauthorized_only
    def login(self, request: request):
        if request.method == "GET":
            return render(request, 'page/auth/login.html', {})
        
        elif request.method == 'POST':
            form = LoginForm(request.POST)

            if form.is_valid():
                dto = form.cleaned_data
                remember = dto['remember']
                del dto['remember']

                user = authenticate(request, email=dto['email'], password=dto['password'])
                if user is not None:
                    login(request, user)
                    
                    if remember:
                        request.session.set_expiry(60 * 60 * 24 * 30)
                    else:
                        request.session.set_expiry(0)
                    
                    return redirect('home')
                else:
                    form.add_error('email', 'Невірний email або пароль.')

            return render(request,  'page/auth/login.html', {'form': form})
    
    @unauthorized_only
    def register(self, request: request):
        if request.method == "GET":
            return render(request, 'page/auth/register.html', {})
        
        elif request.method == 'POST':
            form = RegisterForm(request.POST)

            if form.is_valid():
                data = form.cleaned_data

                if data.get('remember'):
                    request.session.set_expiry(60 * 60 * 24 * 30)
                else:
                    request.session.set_expiry(0)

                return redirect('login')
            else:
                return render(request, 'page/auth/register.html', {'form': form})

    @authorized_only
    def logout(self, request):
        logout(request)
        return redirect('home')

    @authorized_only
    def verify_email(self):
        # TODO: Verify email
        pass