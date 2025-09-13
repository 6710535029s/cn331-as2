from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('userprofile/', views.user_profile_view, name='user_profile'),
    path('book/<int:classroom_id>/', views.booking_page, name='booking_page'),
    path('home/', views.home_view, name='home'),
]
