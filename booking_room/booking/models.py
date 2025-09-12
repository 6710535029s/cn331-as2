from django.db import models
from django.contrib.auth.models import User

class Classroom(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    total_hours = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.classroom.name} - {self.date} - {self.hour}"
