# from django.contrib import admin
# from .models import Subject,Assignment,Marks
# # Register your models here.

# admin.site.register(Subject)
# admin.site.register(Assignment)
# admin.site.register(Marks)

from django.contrib import admin
from .models import Subject, Assignment, Marks,Notice

# Register your models here.
admin.site.register(Subject)
admin.site.register(Assignment)
@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "subject",
        "exam_name",
        "marks_obtained",
        "full_marks",
    )


admin.site.register(Notice)