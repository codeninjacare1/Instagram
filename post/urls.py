from django.urls import path
from post.views import index, NewPost, PostDetail, Tags, like, favourite, add_comment
from . import views
from rest_framework.routers import DefaultRouter
from .api_views import TagViewSet, PostFileContentViewSet, PostViewSet, LikesViewSet, FollowViewSet, StreamViewSet, StoryViewSet, SavedPostViewSet
from django.urls import include

router = DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'postfilecontents', PostFileContentViewSet)
router.register(r'posts', PostViewSet)
router.register(r'likes', LikesViewSet)
router.register(r'follows', FollowViewSet)
router.register(r'streams', StreamViewSet)
router.register(r'stories', StoryViewSet)
router.register(r'savedposts', SavedPostViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('newpost', NewPost, name='newpost'),
    path('<uuid:post_id>', PostDetail, name='post-details'),
    path('tag/<slug:tag_slug>', Tags, name='tags'),
    path('<uuid:post_id>/like/', like, name='like'),
    path('<uuid:post_id>/favourite', favourite, name='favourite'),
    path('delete-post/<uuid:post_id>/', views.delete_post, name='delete-post'),
    # path('add_post/', views.add_post, name='add_post'),
    path('add_story/', views.add_story, name='add_story'),
    path('share-post/<uuid:post_id>/<int:user_id>/', views.share_post, name='share-post'),
    path('save-post/<uuid:post_id>/', views.save_post, name='save-post'),
    path('toggle-favourite/<uuid:post_id>/', views.toggle_favourite, name='toggle-favourite'),
    path('add-comment/<uuid:post_id>/', add_comment, name='add-comment'),
    path('api/', include(router.urls)),
]
