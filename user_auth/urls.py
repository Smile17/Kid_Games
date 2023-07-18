from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.SignUpView.as_view(), name='register'),
]