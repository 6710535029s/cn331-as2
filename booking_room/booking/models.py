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
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f"{self.code} - {self.name}"

class Booking(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    hour = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('classroom', 'date', 'hour')
        verbose_name = "การจองห้องเรียน"
        verbose_name_plural = "การจองห้องเรียนทั้งหมด"

    def __str__(self):
        return f"{self.classroom.code} | {self.date} | {self.hour}"
