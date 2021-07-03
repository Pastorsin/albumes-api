from django.contrib.auth import get_user_model
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers
from user.models import Settings


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['color_mode', 'elements_per_page', 'font_size']
        # FIXME - https://github.com/axnsan12/drf-yasg/issues/239
        ref_name = None


class BaseUserSerializer(WritableNestedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'first_name', 'last_name', 'settings']
        read_only_fields = ['id', 'email', 'first_name', 'last_name']

        abstract = True


class UserSerializer(BaseUserSerializer):
    settings = SettingsSerializer()
