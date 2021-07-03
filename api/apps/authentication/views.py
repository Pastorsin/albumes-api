from rest_social_auth.views import BaseSocialAuthView
from authentication.serializers import AuthSerializer


class AuthView(BaseSocialAuthView):
    serializer_class = AuthSerializer
