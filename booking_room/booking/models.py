from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

class Classroom(models.Model):
    STATUS_CHOICES = [
        ('available', 'เปิดให้จอง'),
        ('unavailable', 'ไม่พร้อมใช้งาน'),
        ('maintenance', 'ปิดปรับปรุง'),
    ]
    code = models.CharField(max_length=20, unique=True, default='RM000')
    name = models.CharField(max_length=100, default='ห้องเรียนทั่วไป')
    capacity = models.PositiveIntegerField(default=30)
    available_hours = models.PositiveIntegerField(default=8)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f"{self.code} - {self.name}"

class Booking(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('date', 'classroom', 'start_time')

    def __str__(self):
        return f"{self.classroom.code} | {self.date} | {self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')} | {self.user.username}"
