from django.contrib import admin
from django.urls import path, include
#from django.views.generic import TemplateView
from ares import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.profile, name="profile"),
    path('home/', views.homepage, name="home"),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('add_product/', views.add_product, name="addproduct"),
    path('cart/', views.cart, name="cart"),
    path('<str:slug>', views.productView, name="productView"),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
