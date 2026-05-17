from rest_framework import serializers
from .models import GalleryItem, Inquiry, Testimonial
from datetime import date

class GalleryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryItem
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = '__all__'

    # BUSINESS RULE VALIDATION (Criterion 7) 
    def validate_event_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("The event date cannot be in the past.")
        return value

    def validate_guest_count(self, value):
        if value <= 0:
            raise serializers.ValidationError("Guest count must be at least 1.")
        return value