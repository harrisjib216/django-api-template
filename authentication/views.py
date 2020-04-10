# django and api modules
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions


# app modules
from .models import (
    User,
)
from .help_modules import (
    validate_fields,
)
from .serializers import (
    AuthenticatedUserSerializer,
)


# third party
look_up_status = {
    "ok": status.HTTP_200_OK,
    "created": status.HTTP_201_CREATED,
    "accepted": status.HTTP_202_ACCEPTED,
    "unauthorized": status.HTTP_401_UNAUTHORIZED,
    "forbidden": status.HTTP_403_FORBIDDEN,
    "not_found": status.HTTP_404_NOT_FOUND,
    "not_allowed": status.HTTP_405_METHOD_NOT_ALLOWED,
    "server_error": status.HTTP_500_INTERNAL_SERVER_ERROR,
}


# authentication
class Authentication(APIView):

    """
        TODO:
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAdminUser]
    """

    # returns user schema when successful
    def send_authenticated_user(self, user):
        response = AuthenticatedUserSerializer(user, many=True).data
        status = look_up_status.get("accepted")
        return Response(response, status=status)


    # GET: login/get user object
    def get(self, request):
        body = request.POST

        # get basic user login
        username = body.get("username")
        email = body.get("email")
        password = body.get("password")

        # whitelist required fields, validate fields
        required_fields = validate_fields({
            "sign_in_nane": username or email,
            "password": password,
        })

        # return errors when there are malformed required_fields
        if len(required_fields):
            response = {
                "error": "Missing Required Fields",
                "objects": required_fields,
            }
            status = look_up_status.get("not_allowed")
            return Response(response, status=status)

        # login with username
        if username:
            user = User.objects.filter(
                username=username,
                password=password
            )

            if user:
                return self.send_authenticated_user(user)

        # login with email
        if email:
            user = User.objects.filter(
                email=email,
                password=password
            )

            if user:
                return self.send_authenticated_user(user)

        # return failed login if attemptee
        # pasts both check points
        response = {
            "error": "Incorrect Login"
        }
        status = look_up_status.get("unauthorized")

        # send errored or successful response with
        # error/successful objects
        # successful objects for authenticated users
        # is the user's schema
        return Response(response, status=status)


    # POST: create an account
    def post(self, request):
        body = request.POST

        # authentication.models.User fields
        # from sign up request
        first_name = body.get("first_name")
        last_name = body.get("last_name")
        username = body.get("username")
        email = body.get("email")
        password = body.get("password")

        # whitelist required fields, validate fields
        required_fields = validate_fields({
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email": email,
            "password": password,
        })

        # return errors when there are malformed required_fields
        if len(required_fields):
            response = {
                "error": "Missing Required Fields",
                "objects": required_fields,
            }
            status = look_up_status.get("not_allowed")
            return Response(response, status=status)

        # find an existing account or create a new on
        existing_user, created_user = User.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
        )

        # found user with same credentials
        # return creation error
        if existing_user:
            response = {
                "error": "Account already exists",
            }
            status = look_up_status.get("not_allowed")

        # created new user
        # return user object from AuthenticatedUserSerializer
        if created_user:
            response = AuthenticatedUserSerializer(created_user, many=True).data
            status = look_up_status.get("accepted")

        # send errored or successful response with
        # error/successful objects
        # successful objects for authenticated users
        # is the user's schema
        return Response(response, status=status)


