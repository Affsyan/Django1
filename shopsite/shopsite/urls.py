
from django.contrib import admin
from django.urls import path, include
from .views import index, contacts
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('admin_staff/', include('adminapp.urls', namespace='admin_staff')),
    path('contacts/', contacts, name="contacts"),
    path('products/', include('mainapp.urls', namespace="products")),
    path('basket/', include('basketapp.urls', namespace="basket")),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('order/', include('ordersapp.urls', namespace='order')),
    path('', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
