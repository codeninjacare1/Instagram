from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .api_views import StoryViewSet
from django.urls import include

app_name = 'storyapp'

router = DefaultRouter()
router.register(r'stories', StoryViewSet)

urlpatterns = [
    path('add_story/', views.AddStoryView.as_view(), name='add_story'),
    path('story/<int:pk>/', views.StoryDetailView.as_view(), name='story_detail'),
    path('delete_story/<int:pk>/', views.DeleteStoryView.as_view(), name='delete_story'),
    path('api/', include(router.urls)),
] 