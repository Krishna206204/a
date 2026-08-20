from django.contrib import admin
from .models import ClassRoom,Student
# Register your models here.

# admin.site.register(ClassRoom)
@admin.register(ClassRoom)
class classRoomAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'section',
        'teacher',
    )
    
# admin.site.register(Student)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'classroom',
        'address',
        'phone',
        'date_of_birth',
        
    )