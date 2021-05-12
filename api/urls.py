from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view


admin.autodiscover()

router = routers.DefaultRouter()

redoc_view = TemplateView.as_view(
    template_name='redoc.html',
    extra_context={'schema_url': 'openapi-schema'}
)

schema_view = get_schema_view(
    title="Albums API",
    description="API for managing natural disasters albums",
    version="1.0"
)

urlpatterns = [
    path('', redoc_view, name='swagger-ui'),
    path('openapi/', schema_view, name='openapi-schema'),
    path("admin/", admin.site.urls),
    path("interviews/", include('interview.urls')),
]
