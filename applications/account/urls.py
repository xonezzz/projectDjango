from django.urls import path 

from applications.account.views import LoginApiView, RegisterApiView

urlpatterns = [
  path('register/', RegisterApiView.as_view()),
  path('login/', LoginApiView.as_view())
]