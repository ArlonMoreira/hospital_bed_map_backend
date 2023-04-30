from django.urls import re_path
from .views import LoginView, RefreshTokenView

urlpatterns = [
    re_path('login/', LoginView.as_view()),
    re_path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    #re_path('logout/', LogoutView.as_view())
]