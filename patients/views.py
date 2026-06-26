from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response

from .models import Insurance, MedicalRecord, Patient
from .serializers import InsuranceSerializer, MedicalRecordSerializer, PatientSerializer

# GET /api/patients/ - List all patients
# POST /api/patients/ - Create a new patient
# GET /api/patients/<pk>/ - Retrieve a specific patient
# PUT /api/patients/<pk>/ - Update a specific patient
# DELETE /api/patients/<pk>/ - Delete a specific patient


@api_view(["GET", "POST"])
def ListPatients(request):
    if request.method == "GET":
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # return Response(serializer.data, status=201)
        return Response(status=status.HTTP_201_CREATED)
        # return Response(status=status.HTTP_400_BAD_REQUEST)


class ListPatientsView(ListAPIView, CreateAPIView):
    """
    Obtiene la lista de pacientes y permite crear un nuevo paciente
    """

    allowed_methods = ["GET", "POST"]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    """def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
"""


"""
class DetailPatientView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
"""

"""
class DetailPatientView(APIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        patient = self.get_object(pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

"""
@api_view(["GET", "PUT", "DELETE"])
def DetailPatient(request, pk):
    try:
        patient = Patient.objects.get(id=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = PatientSerializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    if request.method == "DELETE":
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

"""
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
from .models import Patient, Insurance, MedicalRecord
"""


class ListPatientView(ListAPIView, CreateAPIView):
    allowed_methods = ["GET", "POST"]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class DetailPatientView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class ListInsuranceView(ListAPIView, CreateAPIView):
    allowed_methods = ["GET", "POST"]
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()


class DetailInsuranceView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()


class ListMedicalRecordView(ListAPIView, CreateAPIView):
    allowed_methods = ["GET", "POST"]
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()


class DetailMedicalRecordView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()
