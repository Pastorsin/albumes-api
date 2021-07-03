from django.contrib import admin
from django.urls import path, include
from doc.views import redoc_view


urlpatterns = [
    path('', redoc_view),
    path('admin/', admin.site.urls),
    path('docs/', include('doc.urls')),
    path('interviews/', include('interview.urls')),
    path('albums/', include('album.urls')),
    path('users/', include('user.urls')),
    path('auth/', include('authentication.urls')),
]
