from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from bookings.models import Appointment
from bookings.serializers import AppointmentSerializer
from doctors.models import Department, Doctor, DoctorAvailability, MedicalNote
from doctors.serializers import (
    DepartmentSerializer,
    DoctorAvailabilitySerializer,
    DoctorSerializer,
    MedicalNoteSerializer,
)

from .permissions import IsDoctor


class DoctorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing doctor instances.
    """

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated, IsDoctor]

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

    @action(
        ["GET", "POST", "DELETE"],
        detail=True,
        serializer_class=AppointmentSerializer,
        url_path="appointments(?:/(?P<appointment_id>[^/.]+))?",
    )
    def appointments(self, request, pk=None):
        doctor = self.get_object()

        if request.method == "GET":
            appointments = Appointment.objects.filter(doctor=doctor)
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data)
        elif request.method == "POST":
            data = request.data.copy()  # Hacemos una copia de los datos de la solicitud
            data["doctor"] = doctor.id  # Agregamos el ID del doctor a los datos
            serializer = AppointmentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save(doctor=doctor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif request.method == "DELETE" and appointment_id:
            try:
                appointment = Appointment.objects.get(id=appointment_id)
                serializer = self.serializer_class(appointment)
                appointment.delete()
                return Response(status=status.HTTP_200_OK)

            except Appointment.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)


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
