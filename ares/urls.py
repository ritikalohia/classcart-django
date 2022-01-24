from django.urls import path
from . import views 

urlpatterns = [
    path('home/', views.homepage, name="home"),
    path('add_product/', views.add_product, name="addproduct"),
    path('<str:slug>', views.productView, name="productView"),
]