from django.shortcuts import render

# Create your views here.
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
from .models import Patient, Insurance, MedicalRecord

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView


# GET /api/patients => Listar
# POST /api/patients => Crear
# GET /api/patients/<id>/ => Detalle
# PUT /api/patients/<id>/ => ModificaciÃ³n
# DELETE /api/patients/<id>/ => Borrar


# @api_view(["GET", "POST"])
# def list_patients(request):
#     if request.method == "GET":
#         patients = Patient.objects.all()
#         serializer = PatientSerializer(patients, many=True)
#         return Response(serializer.data)

#     if request.method == "POST":
#         serializer = PatientSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED)


class ListPatientsView(ListAPIView, CreateAPIView):
    allowed_methods = ["GET", "POST"]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    # def get(self, request):
    #     patients = Patient.objects.all()
    #     serializer = PatientSerializer(patients, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = PatientSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(["GET", "PUT", "DELETE"])
# def detail_patient(request, id):
#     try:
#         patient = Patient.objects.get(id=id)
#     except Patient.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = PatientSerializer(patient)
#         return Response(serializer.data)

#     if request.method == "PUT":
#         serializer = PatientSerializer(patient, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     if request.method == "DELETE":
#         patient.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class DetailPatientView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "PATCH", "DELETE"]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    # def get(self, request, id):
    #     try:
    #         patient = Patient.objects.get(id=id)
    #     except Patient.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    #     serializer = PatientSerializer(patient)
    #     return Response(serializer.data)

    # def put(self, request, id):
    #     try:
    #         patient = Patient.objects.get(id=id)
    #     except Patient.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    #     serializer = PatientSerializer(patient, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def delete(self, request, id):
    #     try:
    #         patient = Patient.objects.get(id=id)
    #     except Patient.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    #     patient.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


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
