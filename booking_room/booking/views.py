from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Classroom, Booking
from django.utils import timezone
from datetime import datetime, time, timedelta

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

# รายการจองของผู้ใช้ (ถ้ามีหน้าแยก)
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})

# ยกเลิกการจอง
@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('user_profile')

    
# ติดต่อส่งชื่อ username ไปที่ user_profile
@login_required(login_url='login')
def user_profile_view(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/user_profile.html', {'bookings': bookings})

    
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

# หน้าจองห้อง
@login_required
def booking_page(request, classroom_id):
    room = get_object_or_404(Classroom, id=classroom_id)

    if request.method == 'POST':
        date_str = request.POST.get('date')
        time_str = request.POST.get('time_slot')

        if not date_str or not time_str:
            messages.error(request, "กรุณาเลือกวันที่และช่วงเวลา")
        else:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            start_time = datetime.strptime(time_str, "%H:%M").time()
            end_time = (datetime.combine(date, start_time) + timedelta(hours=1)).time()

            # ตรวจสอบว่าช่วงเวลานี้ถูกจองแล้วหรือยัง
            if Booking.objects.filter(classroom=room, date=date, start_time=start_time).exists():
                messages.error(request, "ช่วงเวลานี้ถูกจองแล้ว")
            else:
                Booking.objects.create(
                    classroom=room,
                    date=date,
                    start_time=start_time,
                    end_time=end_time,
                    user=request.user
                )
                messages.success(request, "จองห้องเรียนเรียบร้อยแล้ว")
                return redirect('user_profile')

    context = {
        'room': room,
    }
    return render(request, 'booking/my_booking.html', context)

