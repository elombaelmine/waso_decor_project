from django.db import models

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

    client_name = models.CharField(max_length=200)
    client_email = models.EmailField()
    event_date = models.DateField()
    venue_name = models.CharField(max_length=255)
    guest_count = models.IntegerField()
    budget_estimate = models.DecimalField(max_digits=10, decimal_places=2)
    color_palette = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.client_name} for {self.event_date}"
    
class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    content = models.TextField()
    is_visible = models.BooleanField(default=False) # The toggle for the live site

    def __str__(self):
        return self.client_name