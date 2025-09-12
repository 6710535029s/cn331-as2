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
    

