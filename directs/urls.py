from directs.views import Directs, SendDirect, UserSearch, NewConversation
from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from .api_views import MessageViewSet

router = DefaultRouter()
router.register(r'messages', MessageViewSet)


urlpatterns = [
    path('', Directs, name="message"),
    path('direct/<username>', Directs, name="directs"),
    path('send/', SendDirect, name="send-directs"),
    path('search/', UserSearch, name="search-users"),
    path('new/<username>', NewConversation, name="conversation"),
    path('api/', include(router.urls)),
]



