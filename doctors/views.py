# Create your views here.
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import (
    Department,
    Doctor,
    DoctorAvailability,
    MedicalNote,
)
from .serializers import (
    DepartmentSerializer,
    DoctorAvailabilitySerializer,
    DoctorSerializer,
    MedicalNoteSerializer,
)


class ListDoctorView(ListAPIView, CreateAPIView):
    allowed_methods = ["GET", "POST"]
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class DetailDoctorView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class ListDepartmentView(ListAPIView, CreateAPIView):
    allowed_methods = ["GET", "POST"]
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DetailDepartmentView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class ListDoctorAvailabilityView(ListAPIView, CreateAPIView):
    allowed_methods = ["GET", "POST"]
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class DetailDoctorAvailabilityView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class ListMedicalNoteView(ListAPIView, CreateAPIView):
    allowed_methods = ["GET", "POST"]
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()


class DetailMedicalNoteView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()
