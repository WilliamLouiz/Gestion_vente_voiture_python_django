# noinspection PyUnresolvedReferences
from django.contrib import admin
from django.conf import settings
# noinspection PyUnresolvedReferences
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("client.urls")),
    path('voiture/', include('voiture.urls')),
    path('vente/', include('vente.urls')),
    path('stat/', include('vente.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
