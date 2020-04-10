# django imports
from django.contrib import admin


# models
from .models import (
    User
)


# Register your models here.
admin.register(User)