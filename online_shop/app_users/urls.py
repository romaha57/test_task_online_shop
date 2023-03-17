from django.urls import path

from .views import (UserLoginView, UserLogoutView, UserProfileView,
                    UserRegistrationView)

app_name = 'app_users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('signup/', UserRegistrationView.as_view(), name='sign_up'),
    path('profile/<str:email>', UserProfileView.as_view(), name='profile'),
]
