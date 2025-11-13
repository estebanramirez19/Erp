from django.contrib import admin
from django.urls import path, include
from usuarios import views as usuarios_views  # <– importante

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', usuarios_views.home, name='home'),  # o lo que uses como inicio
    path('productos/', include('productos.urls')),  # CRUD real
]
