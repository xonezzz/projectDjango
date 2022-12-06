from django.urls import path

from applications.account.views import ForgotPasswordAPIView, ForgotPasswordCompleteAPIView, LoginApiView, RegisterApiView, LogoutApiView, ChangePasswordApiView, \
    send_hello_api_view, ActivationApiView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('login/', LoginApiView.as_view()),
    # path('logout/', LogoutApiView.as_view()),
    path('change_password/', ChangePasswordApiView.as_view()),
    path('send_mail/', send_hello_api_view),
    path('activate/<uuid:activation_code>/', ActivationApiView.as_view()),
    path('forgot_password/', ForgotPasswordAPIView.as_view()),
    path('forgot_password_complete/', ForgotPasswordCompleteAPIView.as_view())
]

