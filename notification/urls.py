from django.urls import path, include
from notification.views import ShowNotification, DeleteNotification

from rest_framework.routers import DefaultRouter
from .api_views import NotificationViewSet

router = DefaultRouter()
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', ShowNotification, name='show-notification'),
    path('<noti_id>/delete', DeleteNotification, name='delete-notification'),
    path('api/', include(router.urls)),
]