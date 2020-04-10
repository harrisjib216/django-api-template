# django import
from django.contrib import admin
from django.urls import path


# url imports
from authentication.urls import _URL_PATTERNS


# define url patterns for Django
urlpatterns = [
    # app urls
    path('admin/', admin.site.urls),

    # project urls
    *_URL_PATTERNS,
]
