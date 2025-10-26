from django.contrib import admin
from .models import Role, User

class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'access_level') 
    search_fields = ('name',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email')
    search_fields = ('full_name', 'email')

admin.site.register(Role, RoleAdmin)
admin.site.register(User, UserAdmin)