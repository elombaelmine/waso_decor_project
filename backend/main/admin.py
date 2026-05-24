from django.contrib import admin
from .models import GalleryItem, Inquiry, Testimonial, UserProfileOTP


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