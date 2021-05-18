from album.views import AlbumViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('', AlbumViewSet, basename='album')
urlpatterns = router.urls
