from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Classroom, Booking
from datetime import time

# หน้าแรกของระบบ (หลัง login)
def home_view(request):
    classrooms = Classroom.objects.filter(status='available')
    return render(request, 'booking/home.html', {'classrooms': classrooms})
    
# หน้าโปรไฟล์ผู้ใช้
@login_required(login_url='login')
def user_profile_view(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/user_profile.html', {'bookings': bookings})

# หน้าจองห้องเรียน
@login_required(login_url='login')
def booking_page(request, classroom_id):
    classroom = get_object_or_404(Classroom, id=classroom_id)
    
return render(request, 'booking/booking_page.html', context)







