from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.student, name="student"),
    path("portal/", views.student_lookup, name="student-lookup"),
    path("portal/<int:student_id>/", views.student_dashboard, name="student-dashboard"),
    path("portal/<int:student_id>/marks/", views.student_marks, name="student-marks"),
    path(
        "portal/<int:student_id>/attendance/",
        views.student_attendance,
        name="student-attendance",
    ),
    path(
        "portal/<int:student_id>/report-card/<str:exam_name>/",
        views.student_report_card,
        name="student-report-card",
    ),
    
# Added manually
    path("accounts/logout/", views.student_logout, name="student-logout"),   
]

# the teacher logout is changed to the teacher_logout to the views.py 
# urls.py and sidebar  and same thing is done for the student 
# to make more effective and smooth access of the login and logout