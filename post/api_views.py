from rest_framework import viewsets
from .models import Tag, PostFileContent, Post, Likes, Follow, Stream, Story, SavedPost
from .serializers import TagSerializer, PostFileContentSerializer, PostSerializer, LikesSerializer, FollowSerializer, StreamSerializer, StorySerializer, SavedPostSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PostFileContentViewSet(viewsets.ModelViewSet):
    queryset = PostFileContent.objects.all()
    serializer_class = PostFileContentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class LikesViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

class StreamViewSet(viewsets.ModelViewSet):
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

class SavedPostViewSet(viewsets.ModelViewSet):
    queryset = SavedPost.objects.all()
    serializer_class = SavedPostSerializer 