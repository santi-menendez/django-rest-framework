from rest_framework import viewsets

from doctors.models import Department, Doctor, DoctorAvailability, MedicalNote
from doctors.serializers import (
    DepartmentSerializer,
    DoctorAvailabilitySerializer,
    DoctorSerializer,
    MedicalNoteSerializer,
)


class DoctorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing doctor instances.
    """

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing department instances.
    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing doctor availability instances.
    """

    queryset = DoctorAvailability.objects.all()
    serializer_class = DoctorAvailabilitySerializer


class MedicalNoteViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing medical note instances.
    """

    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer
