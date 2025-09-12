from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('book/', views.book_room_view, name='book_room'),
    path('my-bookings/', views.my_bookings_view, name='my_bookings'),
]
