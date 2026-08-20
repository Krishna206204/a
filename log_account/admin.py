from django.contrib import admin
from .models import ActivityLog


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):

    list_display = (
        'log_id',
        'user',
        'user_name',
        'user_role',
        'action_type',
        'method',
        'path',
        'status_code',
        'ip_address',
        'timestamp',
    )

    list_filter = (
        'action_type',
        'method',
        'status_code',
    )

    search_fields = (
        'user__username',
        'user__first_name',
        'user__last_name',
        'action_type',
        'path',
        'ip_address',
        'description',
    )

    ordering = ('-timestamp',)

    readonly_fields = (
        'log_id',
        'user',
        'user_name',
        'user_role',
        'action_type',
        'alert_message',
        'path',
        'method',
        'status_code',
        'ip_address',
        'description',
        'timestamp',
    )

    list_per_page = 25

    # Show user's full name
    @admin.display(description='Name')
    def user_name(self, obj):
        if not obj.user:
            return "Unknown"

        full_name = f"{obj.user.first_name} {obj.user.last_name}".strip()

        if full_name:
            return full_name

        return obj.user.username

    # Show Student / Teacher / Admin
    @admin.display(description='User Type')
    def user_role(self, obj):
        if not obj.user:
            return "Unknown"

        # Superuser/Admin
        if obj.user.is_superuser:
            return "Admin"

        # Custom role field
        if hasattr(obj.user, 'role') and obj.user.role:
            return obj.user.role.capitalize()

        return "User"