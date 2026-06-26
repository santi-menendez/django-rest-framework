from datetime import date, datetime

from rest_framework import serializers

from bookings.serializers import AppointmentSerializer

from .models import Insurance, MedicalRecord, Patient


class PatientSerializer(serializers.ModelSerializer):
    appointments = AppointmentSerializer(many=True, read_only=True)
    age = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        # fields = "__all__"
        fields = [
            "id",
            "first_name",
            "last_name",
            "age",
            "date_of_birth",
            "contact_number",
            "email",
            "address",
            "medical_history",
            "appointments",
        ]

    def get_age(self, obj):
        age_td = date.today() - obj.date_of_birth
        years = age_td.days // 365
        return f"{years} años"

    def validate_date_of_birth(self, value):
        today = datetime.date.today()
        age = (
            today.year
            - value.year
            - ((today.month, today.day) < (value.month, value.day))
        )
        if age >= 18:
            return value
        raise serializers.ValidationError("El paciente debe tener al menos 18 años")


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = "__all__"


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = "__all__"
