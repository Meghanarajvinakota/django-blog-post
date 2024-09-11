from django.contrib import admin
from .models import Share
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class ShareAdmin(admin.ModelAdmin):
    list_display = ('title', 'approved')  # Display title and approved status
    list_filter = ('approved',)  # Add filter by approval status
    actions = ['approve_shares']  # Register the custom action

    def approve_shares(self, request, queryset):
        queryset.update(approved=True)  # Approve selected shares
        self.message_user(request, "Selected shares have been approved.")  # Confirmation message

    approve_shares.short_description = "Approve selected shares"  # Description for the action

admin.site.register(Share, ShareAdmin)
