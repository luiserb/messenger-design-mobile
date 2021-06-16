from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('', include('backend.apps.core.urls')),
    path('', include('backend.apps.chatbot.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
