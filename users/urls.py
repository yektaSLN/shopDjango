from django.urls import path
from .views import (
    RegisterView,
    MyTokenObtainPairView,
    UserListView,
    UserStatusUpdateView,
    PasswordResetView
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    #uuth
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #user management
    path('list/', UserListView.as_view(), name='user_list'),
    path('status/<int:id>/', UserStatusUpdateView.as_view(), name='user_status_update'),

    #forgot password
    path('forgot-password/', PasswordResetView.as_view(), name='forgot_password'),
]
