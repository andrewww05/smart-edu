from apps.users.models import User, Role
from smartedu.common.constants import AccessLevel

class UsersService:
    def __init__(self):
        self._usersRepository = User
        self._userRolesRepository = Role
    
    def exists(self, email):
        return self._usersRepository.objects.filter(email=email).exists(); 

    def create(self, data):
        role = self._userRolesRepository.objects.get(access_level=AccessLevel.GUEST)

        user = self._usersRepository.objects.create_user(
            email=data['email'],
            first_name=data['first_name'],
            second_name=data['second_name'],
            password=data['password'],
            role=role
        )

        return user
