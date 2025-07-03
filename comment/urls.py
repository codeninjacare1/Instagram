from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import CommentViewSet

router = DefaultRouter()
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
] 