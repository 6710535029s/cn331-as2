from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# class room model
class Classroom(models.Model):
    room_code = models.CharField(max_length= 64, unique=True) # กำหนดให้room_codeไม่ซ้ำกัน
    room_name = models.CharField(max_length= 128) # ชื่อห้อง
    room_capacity = models.PositiveIntegerField() # ความจุของห้อง
    available_hours = models.PositiveIntegerField() # ชั่วโมงที่ว่างของห้องนั้น
    status = models.BooleanField(default=True) #ส ถานะขอห้อง ณ ขณะนั้น
    
# booking model
class Booking(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) #เชื่อมโยงกับ user model 
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE) #เชื่อมโยงกับ room model
    booking_date = models.DateField(auto_now_add=True) # วันที่จอง 
    start_time = models.TimeField() # เวลาที่เริ่มจอง
    end_time = models.TimeField() # เวลาที่สิ้นสุดการจอง

