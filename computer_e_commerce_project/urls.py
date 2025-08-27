
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_admin/', include('user_admin.urls')),
    path('', include('exposed_wires_app.urls')), 
    path('accounts/', include('registration.urls')),
    path('api/', include('api.urls')),
]
                                