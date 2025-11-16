from django.contrib.auth import authenticate, login
from apps.users.service import UsersService
from smartedu.common.constants.exception_texts import ExceptionText


class AuthService:
    def __init__(self):
        self._usersService = UsersService()

    def login_user(self, request, dto):
        remember = dto.pop('remember')

        user = authenticate(request, email=dto['email'], password=dto['password'])
        if not user:
            return {
                'success': False,
                'error': ExceptionText.WRONG_CREDENTIALS
            }

        login(request, user)

        if remember:
            request.session.set_expiry(60 * 60 * 24 * 30)
        else:
            request.session.set_expiry(0)

        return {
            'success': True,
        }
    
def register_user(self, request, dto):
    try:
        remember = dto.pop('remember')
        user = self._usersService.create(dto)
        
        if not user:
            return {
                'success': False,
                'error': ExceptionText.UNEXPECTED_ERROR
            }
        login(request, user)

        if remember:
            request.session.set_expiry(60 * 60 * 24 * 30)
        else:
            request.session.set_expiry(0)

        return {
            'success': True,
        }
    except Exception:
        return {
            'success': False,
            'error': ExceptionText.UNEXPECTED_ERROR
        }
