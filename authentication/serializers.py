# drf imports
from rest_framework.serializers import (
    ModelSerializer
)

# model imports
from .models import (
    User,
)

# return authenticated users
class AuthenticatedUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "online",
        ]