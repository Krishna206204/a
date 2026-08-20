# from django.contrib import admin
# from .models import Subject,Assignment,Marks
# # Register your models here.

# admin.site.register(Subject)
# admin.site.register(Assignment)
# admin.site.register(Marks)

from django.contrib import admin
from .models import Subject, Assignment, Marks,Notice


# admin.site.register(Subject)
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=(
        "name",
        "classroom",
    )
    
    
# admin.site.register(Assignment)
@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display=(
        'title',
        'description',
        'subject',
        'classroom',
        'created_at',
    )


@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "subject",
        "exam_name",
        "marks_obtained",
        "full_marks",
    )


# admin.site.register(Notice)
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display=(
        'title',
        'description',
        'created_at',
        
    )