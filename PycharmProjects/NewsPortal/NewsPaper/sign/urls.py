from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView
from .views import upgrade_me
from allauth.account.views import ConfirmEmailView


urlpatterns = [
    path('login/', LoginView.as_view(template_name='sign/login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='sign/signup.html'), name='signup'),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('account/', include('allauth.urls')),
    path('account/confirm-email/<str:key>/', ConfirmEmailView.as_view(), name='email_confirmation_subject'),
]