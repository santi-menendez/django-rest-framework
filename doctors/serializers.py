from rest_framework import serializers

from bookings.serializers import AppointmentSerializer, MedicalNoteSerializer

from .models import Department, Doctor, DoctorAvailability, MedicalNote


class DoctorSerializer(serializers.ModelSerializer):
    appointments = AppointmentSerializer(many=True, read_only=True)
    notes = MedicalNoteSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = "__all__"
        fields = [
            "id",
            "first_name",
            "last_name",
            "qualification",
            "contact_number",
            "email",
            "address",
            "biography",
            "is_on_vacation",
            "notes",
            "appointments",
        ]

    def validate_email(self, value):
        if "@example.com" in value:
            return value
        raise serializers.ValidationError("El correo debe incluir @example.com")

    def validate(self, attrs):
        if len(attrs["contact_number"]) < 10 and attrs["is_on_vacation"]:
            raise serializers.ValidationError(
                "Por favor, ingrese un número válido antes de irte a vacaciones"
            )
        return super().validate(attrs)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = "__all__"


class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = "__all__"
