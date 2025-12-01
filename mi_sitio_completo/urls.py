from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls', namespace='usuarios')),  # Rutas de autenticación
    path('blog/', include('blog.urls', namespace='blog')),
    path('galeria/', include('galeria.urls', namespace='galeria')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)