from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('home/', views.home_view, name='home_view'),
    path('userprofile/', views.user_profile_view, name='user_profile'),
    path('profile/', views.user_profile_view, name='user_profile'),  # สำรอง
    path('book/<int:classroom_id>/', views.booking_page, name='booking_page'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
]
