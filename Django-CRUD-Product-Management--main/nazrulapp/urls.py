from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',homePage,name='home'),
    path('product/',productPage,name='product'),
    path('product-edit/<int:id>/',productEditPage,name='productEdit'),
    path('product-delete/<int:id>/',productDeletePage,name='productDelete'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)