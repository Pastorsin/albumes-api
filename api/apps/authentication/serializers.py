from rest_framework import serializers
from rest_social_auth.serializers import TokenSerializer
from user.serializers import BaseUserSerializer, SettingsSerializer


class AuthUserSerializer(BaseUserSerializer):
    settings = SettingsSerializer(read_only=True)


class AuthSerializer(AuthUserSerializer, TokenSerializer):
    provider = serializers.CharField(write_only=True)
    code = serializers.CharField(write_only=True)

    class Meta(AuthUserSerializer.Meta):
        fields = [
            *AuthUserSerializer.Meta.fields,
            'provider', 'code', 'token',
        ]
