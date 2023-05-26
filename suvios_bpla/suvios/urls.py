from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('register/google/', views.google_register, name='google_register'),
    path('register/google/callback/', views.google_callback, name='google_callback'),
]
