from django.db import models
from django.contrib.auth.models import User

class Classroom(models.Model):
     STATUS_CHOICES = [
        ('available', 'เปิดให้จอง'),
        ('unavailable', 'ไม่พร้อมใช้งาน'),
        ('maintenance', 'ปิดปรับปรุง'),
    ]
    code = models.CharField(max_length=20, unique=True, default='RM000'))
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f"{self.code} - {self.name}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.IntegerField()

    def __str__(self):
        return f"{self.classroom.code} | {self.date} | {self.hour}"

