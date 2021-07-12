from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/', include('umsubjects.urls')),
    path('api/', include('authentication.urls')),
    path('api/', include(router.urls)),
]
