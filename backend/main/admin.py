from django.contrib import admin
from .models import GalleryItem, Inquiry, Testimonial, UserProfileOTP
from .models import ChatMessage


# Register your models here.


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'event_date', 'status', 'guest_count')
    list_filter = ('status', 'event_date') # Bonus: Easy filtering for the manager
    search_fields = ('client_name', 'venue_name')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'is_visible')
    list_editable = ('is_visible',) # Bonus: Clickable toggle on the list page

admin.site.register(GalleryItem)


# Your existing admin configurations (GalleryItem, Inquiry, Testimonial)...

# Append this block at the bottom to expose the OTP table
@admin.register(UserProfileOTP)
class UserProfileOTPAdmin(admin.ModelAdmin):
    list_display = ('user', 'otp_code', 'created_at')
    search_fields = ('user__email', 'otp_code')



@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    # Columns displayed in the list view table
    list_display = ('id', 'user', 'sender_name', 'message_snippet', 'is_from_staff', 'created_at')
    
    # Filter sidebar on the right side
    list_filter = ('is_from_staff', 'created_at', 'user')
    
    # Search box functionality to find messages quickly
    search_fields = ('sender_name', 'message', 'user__username', 'user__email')
    
    # Orders the entries so newest notes appear at the top
    ordering = ('-created_at',)

    # Custom column trick to truncate super long sentences in the table
    def message_snippet(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message
    message_snippet.short_description = "Message Content"