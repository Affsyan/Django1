
from django.contrib import admin
from django.urls import path, include
from .views import index, contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('contacts/', contacts, name="contacts"),
    path('products/', include('mainapp.urls', namespace="products")),
]
