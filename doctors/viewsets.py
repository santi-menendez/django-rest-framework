from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(["POST"], detail=True)
    def set_on_vacation(self, request, pk=None, path="set-on-vacation"):
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response({"status": "El doctor está de vacaciones"})

    @action(["POST"], detail=True)
    def set_off_vacation(self, request, pk=None, path="set-off-vacation"):
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({"status": "El doctor NO está de vacaciones"})


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
