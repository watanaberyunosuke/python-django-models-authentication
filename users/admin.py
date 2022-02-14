from django.contrib import admin
from django.contrib.auth.admin import User, UserAdmin
from .models import User

admin.site.register(User, UserAdmin)

