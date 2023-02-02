from .views import UserList
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'user'


auth_urls = [
    # User Authentication
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


user_urls = [
    path('user', UserList.as_view(), name='user_list'),
]

urlpatterns = [
    path('', include(auth_urls)),
    path('', include(user_urls))
]
