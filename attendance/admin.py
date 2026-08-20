from django.contrib import admin
from .models import Attendance
# Register your models here.

# admin.site.register(Attendance)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display=(
        'student',
        'date',
        'status',
    )