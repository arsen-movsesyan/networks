from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import NetworkSerializer
from .models import Network


class NetworkViewset(viewsets.ModelViewSet):
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    permission_classes = [AllowAny]  # Luck of time did not allow me to clean up properly all unneeded apps
