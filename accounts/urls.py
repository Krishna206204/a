# from django.urls import path
# from . import views
# urlpatterns = [
#     path("",views.teacher_login, name='login'),
#     path("logout/",views.teacher_logout, name='logout'),
#     path("dashboard/",views.dashboard, name="dashboard"),
# ]

from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/' ,views.about,name="about"),
    path('contact/', views.contact,name="contact" ),
    path("login/", views.teacher_login, name="login"),
    path("accounts/logout/", views.teacher_logout, name="teacher-logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
   
]