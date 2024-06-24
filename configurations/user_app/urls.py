from django.urls import path , include
from . import views
from .views import ProfilePictureUploadSerializer, ProfilePictureUploadView, UserListView, UserDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('auth/',include('dj_rest_auth.urls')),
    path('auth/registration/',include('dj_rest_auth.registration.urls')),
    path('profile/update/', ProfilePictureUploadView.as_view(), name='profile-update'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),     
    path("deleteUpdateUser/<int:pk>/",views.UserRetrieveUpdateDestroyAPIView.as_view()), #изменить почту/дату рождения/пароль

    path('request-password-reset/', views.PasswordReset.as_view(), name='request-password-reset'),
    path("password-reset/<str:encoded_pk>/<str:token>/", views.ResetPasswordAPI.as_view(), name="reset-password"),
]

