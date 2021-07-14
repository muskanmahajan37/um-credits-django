from django.urls import path, include
from rest_framework import routers

from .views import SubjectsView, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('subjects/', SubjectsView.as_view()),
]
