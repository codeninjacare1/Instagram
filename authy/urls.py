from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from authy.views import UserProfile, EditProfile
from rest_framework.routers import DefaultRouter
from .api_views import ProfileViewSet


urlpatterns = [
    # Profile Section
    path('profile/edit', EditProfile, name="editprofile"),

    # User Authentication
    path('sign-up/', views.register, name="sign-up"),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-out/', auth_views.LogoutView.as_view(template_name="sign-out.html"), name='sign-out'), 
    path('logout/', views.logout_view, name='logout'),
     #reset password uls: 
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('block/<int:user_id>/', views.block_user, name='block_user'),
    path('unblock/<int:user_id>/', views.unblock_user, name='unblock_user'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    
]

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)

from django.urls import include

urlpatterns += [
    path('api/', include(router.urls)),
]
