from django.contrib import admin
from .models import Classroom, Booking 
#ตั้งค่าการแสดงผลของโมเดลห้องเรียน
@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'capacity', 'status']
    search_fields = ['code', 'name']
    list_filter = ['status']
#ตั้งค่าการแสดงผลของโมเดลการจอง
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['classroom', 'user', 'date', 'hour']
    list_filter = ['date', 'classroom']
    search_fields = ['user__username']
