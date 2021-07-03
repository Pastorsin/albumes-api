from django.urls import path, re_path
from doc.views import redoc_view, swagger_view, json_view


urlpatterns = [
    path('redoc/', redoc_view, name='schema-redoc'),
    path('swagger/', swagger_view, name='schema-swagger-ui'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            json_view, name='schema-json'),
]
