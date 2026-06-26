from rest_framework.routers import DefaultRouter

from .viewsets import (
    DepartmentViewSet,
    DoctorAvailabilityViewSet,
    DoctorViewSet,
    MedicalNoteViewSet,
)

router = DefaultRouter()
router.register("doctors", DoctorViewSet)
router.register("departments", DepartmentViewSet)
router.register("doctoravailabilities", DoctorAvailabilityViewSet)
router.register("medicalnotes", MedicalNoteViewSet)

urlpatterns = [] + router.urls
