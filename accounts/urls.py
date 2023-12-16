"""Defines URL patterns for accounts"""


from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Registration page
    path('register/', views.register, name='register'),
    
    #Password Reset
    path('password_reset/', auth_views.PasswordResetView.as_view(),
          name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), 
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), 
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), 
         name='password_reset_complete'),
    ]
