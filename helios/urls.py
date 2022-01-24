from django.contrib import admin
from django.urls import path, include
from ares import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.profile, name="profile"),
    path('accounts/', include('allauth.urls')),
    path('cart/', include('cart.urls')),
    path(' ', include('ares.urls')),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
