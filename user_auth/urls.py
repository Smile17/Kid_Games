from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('reset_password/', views.CustomPasswordResetView.as_view(), name='reset_password'),
    path('password_reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('custom_password_reset_confirm', views.CustomPasswordResetConfirmView.as_view(), name='custom_password_reset_confirm'),


]