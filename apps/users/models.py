import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from smartedu.common.constants.access_level import AccessLevel

class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    access_level = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'roles'
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return f"{self.name} (Level {self.access_level})"


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, second_name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            second_name=second_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, second_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, first_name, second_name, password, **extra_fields)


class User(AbstractUser):
    username = None  # Remove username field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'second_name']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT,
        related_name='users',
        null=True,
        blank=True,
    )
    email = models.EmailField(max_length=255, unique=True)
    email_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.first_name} {self.second_name} ({self.email})"
    
    def has_access_level(self, required_level):
        return self.role and self.role.access_level >= required_level
    
    def is_admin(self):
        return self.has_access_level(AccessLevel.ADMIN)