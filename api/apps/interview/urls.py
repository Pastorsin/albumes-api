from interview.views import InterviewViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('', InterviewViewSet, basename='interview')
urlpatterns = router.urls
