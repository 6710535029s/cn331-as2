from django.contrib import admin
from .models import Classroom, Booking 

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'capacity', 'status']
    search_fields = ['code', 'name']
    list_filter = ['status']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['classroom', 'user', 'date', 'hour']
    list_filter = ['date', 'classroom']
    search_fields = ['user__username']
