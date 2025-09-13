from django.urls import path
from . import views
from .views import admin_dashboard

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('admin-interface/', admin_dashboard, name='admin_dashboard'),
]
