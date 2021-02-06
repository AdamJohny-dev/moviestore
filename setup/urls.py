from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('apps.moviestore.urls')),
    path('owners/', include('apps.owners.urls')),
    path('clients/', include('apps.clients.urls')),
    path('rented/', include('apps.rented.urls')),
    path('admin/', admin.site.urls),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
