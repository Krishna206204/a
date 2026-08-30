from django.urls import path
from . import views
urlpatterns = [
path("list/",views.today_attendance,name="attendance"),
path("mark/",views.mark_attendance,name="mark-attendance"),
path("history/",views.attendance_history,name="attendance-history"),
path(
        "admin/mark/",
        views.admin_mark_attendance,
        name="admin-mark-attendance"
    ),
path(
    "admin/history/",
    views.admin_attendance_history,
    name="admin-attendance-history"
),
path(
    "admin/today/",
    views.admin_today_attendance,
    name="admin-today-attendance"
),

]