# django module
from django.contrib import admin
from django.conf.urls import url, include


# drf
from rest_framework import routers


# app imports
from .views import (
    Authentication
)


# declare router
router = routers.DefaultRouter(trailing_slash=True)


# declare routes below
# define url patterns
_URL_PATTERNS = [
    url(r"^api/auth/$", Authentication.as_view(), name="authentication"),
]
