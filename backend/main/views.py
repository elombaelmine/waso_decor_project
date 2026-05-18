import secrets
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import GalleryItem, Inquiry, Testimonial
from .serializers import GalleryItemSerializer, InquirySerializer, TestimonialSerializer

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
        if self.request.user.is_staff:
            return Testimonial.objects.all()
        return Testimonial.objects.filter(is_visible=True)


class InquiryViewSet(viewsets.ModelViewSet):
    """
    Handles the Lead Qualification forms.
    Allows anyone to submit an inquiry (creating an account automatically),
    but restricts viewing/listing to authenticated users.
    """
    serializer_class = InquirySerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Inquiry.objects.all().order_by('-created_at')
        return Inquiry.objects.filter(user=self.request.user).order_by('-created_at')

    def create(self, request, *args, **kwargs):
        """
        Intercepts the booking submission to automatically spin up a 
        secure client account if it doesn't exist yet.
        """
        data = request.data
        email = data.get('client_email')
        name = data.get('client_name')

        if not email or not name:
            return Response(
                {"error": "Client name and email are required."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        # 1. Automate account detection/creation logic
        user_exists = User.objects.filter(username=email).exists()
        generated_password = None
        target_user = None

        if not user_exists:
            generated_password = secrets.token_urlsafe(8)  # Secure temp password
            target_user = User.objects.create_user(
                username=email,
                email=email,
                password=generated_password,
                first_name=name
            )
        else:
            target_user = User.objects.get(username=email)

        # 2. Process and save the Inquiry using your existing serializer logic
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            # Link the newly created or fetched user to this inquiry model
            serializer.save(user=target_user)
            
            response_data = {
                "message": "Inquiry submitted successfully!",
                "inquiry": serializer.data,
                "account_created": not user_exists,
            }

            # Return credentials dynamically if it's a new registration
            if generated_password:
                response_data["temporary_password"] = generated_password
                response_data["username"] = email

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)