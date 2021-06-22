from user.views import SettingsViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('settings', SettingsViewSet, basename='settings')
urlpatterns = router.urls
