from django.shortcuts import render, redirect
from django.contrib.auth import logout
from apps.auth.forms import RegisterForm, LoginForm
from apps.auth.decorators import unauthorized_only, authorized_only
from apps.auth.service import AuthService

class AuthController:
    def __init__(self):
        self._authService = AuthService()

    @unauthorized_only
    def login(self, request):
        match(request.method):
            case 'POST':
                form = LoginForm(request.POST)

                if form.is_valid():
                    dto = form.cleaned_data.copy()
                    result = self._authService.login_user(request, dto)

                    if result['success']:
                        return redirect('home')

                    form.add_error('email', result['error'])

                return render(request,  'page/auth/login.html', {'form': form})
            case 'GET':
                return render(request, 'page/auth/login.html', {})
    
    @unauthorized_only
    def register(self, request):
        match(request.method):
            case 'POST':
                form = RegisterForm(request.POST)

                if form.is_valid():
                    dto = form.cleaned_data.copy()
                    result = self._authService.register_user(request, dto)

                    if result['success']:
                        return redirect('home')

                    form.add_error('email', result['error'])
                

                return render(request, 'page/auth/register.html', {'form': form})
            case 'GET':
                return render(request, 'page/auth/register.html', {})

    @authorized_only
    def logout(self, request):
        logout(request)
        return redirect('home')

    @authorized_only
    def verify_email(self):
        # TODO: Verify email
        pass