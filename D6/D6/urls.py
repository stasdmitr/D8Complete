from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', include('simpleapp.urls')),
    path('protect/', include('protect.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
]
