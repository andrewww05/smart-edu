from apps.users.models import User

class UsersService:
    def exists(self, email):
        return User.objects.filter(email=email).exists(); 

    def create(self, dto):
        pass