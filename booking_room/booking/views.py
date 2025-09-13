from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Classroom, Booking
from django.utils import timezone
from datetime import datetime,time
from django.shortcuts import render, redirect, get_object_or_404
from .models import Classroom, Booking
from .forms import BookingForm

# หน้าแรกของระบบ (หลัง login)
@login_required(login_url='login')
def home_view(request):
    classrooms = Classroom.objects.filter(status='available')
    return render(request, 'booking/home.html', {'classrooms': classrooms})

# หน้าโปรไฟล์ผู้ใช้
@login_required(login_url='login')
def user_profile_view(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/user_profile.html', {'bookings': bookings})


# ติดต่อส่งชื่อ username ไปที่ my_booking.py
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('user_profile')

    
# ติดต่อส่งชื่อ username ไปที่ my_booking.py
@login_required(login_url='login')
def user_profile_view(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/my_booking.html', {'bookings': bookings})

    
# cancel booking
@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        # คืน available_hours ให้ห้องเรียน
        duration = (datetime.combine(booking.booking_date, booking.end_time) -
                    datetime.combine(booking.booking_date, booking.start_time)).seconds // 3600
        booking.classroom.available_hours += duration
        booking.classroom.save()
        booking.delete()
        messages.success(request, "ยกเลิกการจองเรียบร้อยแล้ว")
        return redirect('user_profile')

#mybooking
@login_required
def booking_page(request, classroom_id):
    room = get_object_or_404(Classroom, id=classroom_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        # ตรวจสอบว่าช่วงเวลานี้ถูกจองไปแล้วหรือยัง
        if form.is_valid():
            date = form.cleaned_data['date']
            time_slot = form.cleaned_data['time_slot']
            if Booking.objects.filter(room=room, date=date, time_slot=time_slot).exists():
                form.add_error(None, 'ช่วงเวลานี้ถูกจองแล้ว')
            else:
                Booking.objects.create(
                    room=room,
                    date=date,
                    time_slot=time_slot,
                    user=request.user
                )
                return redirect('booking_success')


    context = {
        'room': room,
        
    }

  
    return render(request, 'booking/my_booking.html', context)


