import secrets
from django.db import models
from django.contrib.auth.models import User #importing users 

# Create your models here.
class GalleryItem(models.Model):
    EVENT_TYPES = [
        ('WEDDING', 'Weddings'), # For wedding ceremonies, receptions, and related events
        ('BIRTHDAY', 'Birthdays'), # Simplified from Luxury Birthdays
        ('CORPORATE', 'Corporate Events'), #Events like product launches, corporate parties, or business conferences
        ('MEETING', 'Meetings'), # Added for business meetings or conferences
        ('BURIAL', 'Burial Ceremony'), # Added for burial ceremonies, funerals, or memorial services
        ('GENERAL', 'General Events'), # For joinings, parties, or other ceremonies
    ]
    
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    primary_color = models.CharField(max_length=50) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.event_type}"
    
class Inquiry(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('CONTACTED', 'Contacted'),
        ('BOOKED', 'Booked'),
    ]
    
    # 2. This line right here is added to link the Inquiry to their auto-generated User account
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='inquiry')


    client_name = models.CharField(max_length=200)
    client_email = models.EmailField()
    event_date = models.DateField()
    venue_name = models.CharField(max_length=255)
    town = models.CharField(max_length=100, default="Yaoundé")  # Add this line right here
    guest_count = models.IntegerField()
    venue_name = models.CharField(max_length=255)
    guest_count = models.IntegerField()
    budget_estimate = models.DecimalField(max_digits=10, decimal_places=2)
    color_palette = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW')
    created_at = models.DateTimeField(auto_now_add=True)

    # Add this section to fix the admin dashboard spelling
    class Meta:
        verbose_name = "Inquiry"
        verbose_name_plural = "Inquiries"
    
    # --- ADD THIS AUTOMATION LOGIC HERE ---
    def save(self, *args, **kwargs):
        # Only run this if the inquiry doesn't have a user attached yet
        if not self.user and self.client_email:
            # Check if a user with this email already exists
            user_exists = User.objects.filter(username=self.client_email).exists()
            
            if not user_exists:
                # Generate a temporary password
                generated_password = secrets.token_urlsafe(8)
                
                # Create the user account
                new_user = User.objects.create_user(
                    username=self.client_email,
                    email=self.client_email,
                    password=generated_password,
                    first_name=self.client_name
                )
                self.user = new_user
                
                # For testing clarity in terminal/console logs:
                print(f"\n[AUTOMATION] Created user account for {self.client_email}")
                print(f"[AUTOMATION] Temporary Password: {generated_password}\n")
            else:
                # Link to existing user if email matches a previous client
                self.user = User.objects.get(username=self.client_email)

        # Execute standard Django save behavior
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Inquiry from {self.client_name} for {self.event_date}"
    
class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    content = models.TextField()
    is_visible = models.BooleanField(default=False) # The toggle for the live site

    def __str__(self):
        return self.client_name