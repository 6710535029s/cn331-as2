from django.contrib import admin
from .models import Classroom

@admin.register(Classroom) #ใช้ decorator @admin.register เพื่อบอก Django ว่าเราจะจัดการโมเดล Classroom ด้วยคลาส ClassroomAdmin
class ClassroomAdmin(admin.ModelAdmin):
  # กำหนดว่าในหน้า รายการห้องเรียน (list view) จะแสดงคอลัมน์อะไรบ้าง เช่น: รหัสห้อง, ชื่อห้อง, ความจุ, จำนวนชั่วโมงที่เปิดให้จอง, สถานะเปิด/ปิด
    list_display = ('code', 'name', 'capacity', 'total_hours', 'is_available')
  # เพิ่ม ตัวกรองด้านข้าง ให้ admin สามารถกรองห้องเรียนที่เปิดหรือปิดการจองได้ง่าย ๆ
    list_filter = ('is_available',)
  # เพิ่มช่องค้นหาให้ admin สามารถค้นหาห้องเรียนตาม code หรือ name ได้สะดวก
    search_fields = ('code', 'name')
