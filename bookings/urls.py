from django.urls import path

from .views import (
    ListAppointmentView,
    DetailAppointmentView,
    ListMedicalNoteView,
    DetailMedicalNoteView,
)

urlpatterns = [
    path('appointments/', ListAppointmentView.as_view()),
    path('appointments/<int:pk>/', DetailAppointmentView.as_view()),
    path('medicalnotes/', ListMedicalNoteView.as_view()),
    path('medicalnotes/<int:pk>/', DetailMedicalNoteView.as_view()),
]