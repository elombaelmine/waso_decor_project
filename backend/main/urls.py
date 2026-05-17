from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GalleryItemViewSet, InquiryViewSet, TestimonialViewSet

router = DefaultRouter()
router.register(r'gallery', GalleryItemViewSet)
router.register(r'inquiries', InquiryViewSet, basename='inquiry')
router.register(r'testimonials', TestimonialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]