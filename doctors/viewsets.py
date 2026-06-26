from rest_framework import viewsets

from doctors.models import Doctor
from doctors.serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing doctor instances.
    """

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
