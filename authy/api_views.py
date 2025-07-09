from rest_framework import viewsets
from .models import *
from .serializers import *
 
# Example: Replace with actual model names
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer 