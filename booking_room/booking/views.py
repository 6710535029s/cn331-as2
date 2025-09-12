from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking

# หน้าแรกของระบบ (หลัง login)
def home_view(request):
    return render(request, 'booking/home.html')

# ฟังก์ชันสมัครสมาชิก
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm']
        # ตรวจสอบว่ารหัสผ่านตรงกันหรือไม่
        if password == confirm:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'สมัครสมาชิกสำเร็จ')
            return redirect('login')
        else:
            messages.error(request, 'รหัสผ่านไม่ตรงกัน')
    return render(request, 'booking/register.html')

# ฟังก์ชันเข้าสู่ระบบ
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # ตรวจสอบชื่อผู้ใช้และรหัสผ่าน
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')  # ไปหน้าแรกหลัง login
        else:
            messages.error(request, 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง')
    return render(request, 'booking/login.html')

# ฟังก์ชันออกจากระบบ
def logout_view(request):
    logout(request)
    return redirect('login')
    
# ฟังก์ชันจองห้องเรียน (ต้อง login ก่อน)
@login_required(login_url='login')
def book_room_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            classroom = form.cleaned_data['classroom']
            date = form.cleaned_data['date']
            hour = form.cleaned_data['hour']

            # ตรวจสอบว่าผู้ใช้จองห้องนี้ในเวลานี้ไปแล้วหรือยัง
            if Booking.objects.filter(user=request.user, classroom=classroom, date=date, hour=hour).exists():
                messages.error(request, 'คุณจองห้องนี้ในเวลานี้ไปแล้ว')
            # ตรวจสอบว่าห้องนี้ถูกจองในเวลานี้โดยคนอื่นหรือยัง
            elif Booking.objects.filter(classroom=classroom, date=date, hour=hour).exists():
                messages.error(request, 'เวลานี้ถูกจองไปแล้ว')
            else:
                # บันทึกการจอง
                booking = form.save(commit=False)
                booking.user = request.user
                booking.save()
                messages.success(request, 'จองห้องเรียนสำเร็จ')
                return redirect('my_bookings')
    else:
        form = BookingForm()
    return render(request, 'booking/book_room.html', {'form': form})

# ฟังก์ชันแสดงรายการจองของผู้ใช้
@login_required(login_url='login')
def my_bookings_view(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})

