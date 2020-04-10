# django
from django.db import models


# module
from uuid import uuid4


# app imports
from .help_modules import (
    validate_fields,
    LENGTH,
    LONG_LENGTH,
    BIG_LENGTH,
    SHORT_LENGTH,
    SMALL_LENGTH,
)


# Create your models here.
class BaseModel(models.Model):
    guid = models.CharField(max_length=LENGTH)
    active = models.BooleanField(default=True)

    # generate random guid on save
    def save(self, *args, **kwargs):
        if not self.guid:
            self.guid = uuid4()

        super().save(*args, **kwargs)


# basic user model
class User(BaseModel):
    first_name = models.CharField(max_length=SHORT_LENGTH)
    last_name = models.CharField(max_length=SHORT_LENGTH)
    username = models.CharField(max_length=SHORT_LENGTH)
    email = models.EmailField(max_length=LENGTH)
    password = models.CharField(max_length=LONG_LENGTH)
    phone = models.CharField(max_length=SHORT_LENGTH)
    date_joined = models.DateField(auto_now=True)
    online = models.BooleanField(default=False)

    # override save method for validation
    def save(self, *args, **kwargs):
        # create list of required objects
        required_fields = validate_fields({
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "password": self.password,
        })

        # if there are malformed objects
        # return and error, and the fields
        # with errors
        if len(required_fields):
            raise ValueError(f"Missing Credentials: {required_fields}")

        super().save(*args, **kwargs)

    # return Username - First Name
    # as the tuple key when receiving
    # a User query
    def __str__(self):
        return f"{self.username} - {self.first_name}"
