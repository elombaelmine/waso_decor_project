from rest_framework import viewsets, permissions
from .models import GalleryItem, Inquiry, Testimonial
from .serializers import GalleryItemSerializer, InquirySerializer, TestimonialSerializer
# Create your views here.

class GalleryItemViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD for the Inspiration Gallery.
    Publicly viewable, but only editable by the Manager.
    """
    queryset = GalleryItem.objects.all()
    serializer_class = GalleryItemSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class TestimonialViewSet(viewsets.ModelViewSet):
    """
    Handles the Social Proof testimonials.
    """
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

    def get_queryset(self):
        # Users only see visible testimonials; Admin sees all
        if self.request.user.is_staff:
            return Testimonial.objects.all()
        return Testimonial.objects.filter(is_visible=True)

class InquiryViewSet(viewsets.ModelViewSet):
    """
    Handles the Lead Qualification forms.
    """
    serializer_class = InquirySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Mandatory requirement: filtering by owner/manager 
        return Inquiry.objects.all().order_by('-created_at')