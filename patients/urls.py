from django.urls import path

from .views import (
    ListPatientsView,
    DetailPatientView,
    ListInsuranceView,
    DetailInsuranceView,
    ListMedicalRecordView,
    DetailMedicalRecordView,
)

urlpatterns = [
    path('patients/', ListPatientsView.as_view()),
    path('patients/<int:pk>/', DetailPatientView.as_view()),
    path('insurances/', ListInsuranceView.as_view()),
    path('insurances/<int:pk>/', DetailInsuranceView.as_view()),
    path('medicalrecords/', ListMedicalRecordView.as_view()),
    path('medicalrecords/<int:pk>/', DetailMedicalRecordView.as_view()),
]