from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

# ฟังก์ชันสมัครสมาชิก
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password != confirm:
            messages.error(request, 'รหัสผ่านไม่ตรงกัน')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'มีบัญชีผู้ใช้นี้อยู่แล้ว กรุณาเลือกชื่ออื่น')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'สมัครสมาชิกสำเร็จ')
            return redirect('login')

    return render(request, 'booking/register.html') 

# ฟังก์ชันเข้าสู่ระบบ
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง')
    return render(request, 'booking/login.html') 

# ฟังก์ชันออกจากระบบ
def logout_view(request):
    logout(request)
    return redirect('login')
