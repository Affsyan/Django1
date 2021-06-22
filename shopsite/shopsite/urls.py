
from django.contrib import admin
from django.urls import path, include
from .views import index, contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('contacts/', contacts),
    path('products/', include('mainapp.urls')),
]
