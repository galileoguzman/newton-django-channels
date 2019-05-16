from django.urls import path, include
from rest_framework import routers

from . import views

# URLS configuration for API
router = routers.DefaultRouter()
router.register(r'notifications', views.NotificationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
	path('', views.notifications_list, name='notifications_list'),
]