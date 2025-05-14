from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from doctors.models import Department, Doctor, DoctorAvailability, MedicalNote
from doctors.permissions import IsDoctor
from doctors.serializers import (
    DepartmentSerializer,
    DoctorAvailabilitySerializer,
    DoctorSerializer,
    MedicalNoteSerializer,
)
from bookings.serializers import AppointmentSerializer
from bookings.models import Appointment


class DoctorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing doctor instances.
    """

    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = [IsAuthenticated, IsDoctor]

    @action(methods=["POST"], detail=True, url_path="set-on-vacation")
    def set_on_vacation(self, request, pk=None):
        """
        Set on the vacation status of a doctor.
        """
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response({"status": "vacation on"})

    @action(methods=["POST"], detail=True, url_path="set-off-vacation")
    def set_off_vacation(self, request, pk=None):
        """
        Set off the vacation status of a doctor.
        """
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({"status": "vacation off"})

    @action(["POST", "GET"], detail=True, serializer_class=AppointmentSerializer)
    def appointments(self, request, pk):
        doctor = self.get_object()
        if request.method == "POST":
            data = request.data.copy()
            data["doctor"] = doctor.id
            serializer = AppointmentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if request.method == "GET":
            appointment = Appointment.objects.filter(doctor=doctor)
            serializer = AppointmentSerializer(appointment, many=True)
            return Response(serializer.data)


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing department instances.
    """

    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing DoctorAvailability instances.
    """

    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class MedicalNoteViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing MedicalNote instances.
    """

    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()
