from django.contrib import admin
from .models import Classroom, Booking # ดึง class จาก ไฟล์ models มา

# register ให้ django จัดการข้อมูลใน class นี้ได้
admin.site.register(Classroom) 
admin.site.register(Booking) #
