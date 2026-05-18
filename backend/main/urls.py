from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GalleryItemViewSet, InquiryViewSet, TestimonialViewSet

# Instantiating the DRF Default Router
router = DefaultRouter()

# Registering ViewSets dynamically to generate clean REST paths
router.register(r'gallery', GalleryItemViewSet, basename='galleryitem')
router.register(r'inquiries', InquiryViewSet, basename='inquiry')
router.register(r'testimonials', TestimonialViewSet, basename='testimonial')

urlpatterns = [
    # This automatically maps paths like 'api/gallery/' or 'api/gallery/<id>/'
    path('', include(router.urls)),
]