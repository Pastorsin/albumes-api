from rest_framework import mixins
from rest_framework import viewsets
from user.models import Settings
from user.serializers import SettingsSerializer


class SettingsViewSet(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):

    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
