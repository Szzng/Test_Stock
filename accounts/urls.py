from django.urls import path
# from dj_rest_auth.views import (
#     LoginView, LogoutView, PasswordChangeView, PasswordResetConfirmView,
#     PasswordResetView, UserDetailsView,
# )
# from dj_rest_auth.registration.views import RegisterView

from accounts.views import (LoginView, LogoutView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView,
                            UserDetailsView, RegisterView )
from rest_framework_simplejwt.views import TokenVerifyView
from dj_rest_auth.jwt_auth import get_refresh_view

app_name = 'api/accounts'

urlpatterns = [
    # URLs that do not require a valid token
    path('register/', RegisterView.as_view(), name='rest_login'),
    path('login/', LoginView.as_view(), name='rest_login'),
    path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),

    # URLs that require a user to be logged in with a valid token.
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('user/', UserDetailsView.as_view(), name='rest_user_details'),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),

    # token
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
]
