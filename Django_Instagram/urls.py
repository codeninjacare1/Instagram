"""Django_Instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from authy.views import UserProfile, follow

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('authy.urls')),
    path('comment/', include('comment.urls')),
    path('', include('post.urls')),  # Main feed at root
    path('message/', include('directs.urls')),
    path('notification/', include('notification.urls')),
    path('stories/', include('storyapp.urls')),

    # profile
    path('<username>/', UserProfile, name='profile'),
    path('<username>/saved/', UserProfile, name='profilefavourite'),
    path('<username>/follow/<option>/', follow, name='follow'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

