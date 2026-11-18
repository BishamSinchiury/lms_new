
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from apps.authentication.models import User, UserRole


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        trim_whitespace=False,
        style={"input_type": "password"},
        validators=[validate_password],
    )

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "role",
        ]
        read_only_fields = ["id", "role"]

    def validate_email(self, value):
        return value.strip().lower()

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user
