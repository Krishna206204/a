from django.urls import path
from .views import LogActivityListView

urlpatterns = [
    path(
        'admin/account_log/',
        LogActivityListView.as_view(),
        name='activity-log'
    ),
]