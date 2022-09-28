from django.urls import path
from .views import *
from django.contrib.auth import views as auth_vw
from .views import Signup



urlpatterns=[
	path('', home, name='home'),
	path('deposit/', deposit, name='deposit'),
	path('login/', auth_vw.LoginView.as_view(template_name='login.html'), name='login'),
	path('register/', Signup.as_view(), name='register'),
	path('logout/', auth_vw.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password-reset/', auth_vw.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_vw.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_vw.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_vw.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    
	
	]