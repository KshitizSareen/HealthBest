from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions,authentication
from .serializers import UserSerializer,DiseaseSerialzer
from .models import Diseases
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DiseaseViewSet(viewsets.ModelViewSet):
    queryset=Diseases.objects.all()
    serializer_class=DiseaseSerialzer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[authentication.TokenAuthentication]