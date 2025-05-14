from django.urls import path

# from .views import (
#     ListDoctorView,
#     DetailDoctorView,
#     ListDepartmentView,
#     DetailDepartmentView,
#     ListDoctorAvailabilityView,
#     DetailDoctorAvailabilityView,
#     ListMedicalNoteView,
#     DetailMedicalNoteView,
# )

from rest_framework.routers import DefaultRouter
from doctors.viewsSets import (
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

urlpatterns = router.urls


# urlpatterns = [
#     path("doctors/", ListDoctorView.as_view()),
#     path("doctors/<int:pk>/", DetailDoctorView.as_view()),
#     path("departments/", ListDepartmentView.as_view()),
#     path("departments/<int:pk>/", DetailDepartmentView.as_view()),
#     path("doctoravailabilities/", ListDoctorAvailabilityView.as_view()),
#     path("doctoravailabilities/<int:pk>/", DetailDoctorAvailabilityView.as_view()),
#     path("medicalnotes/", ListMedicalNoteView.as_view()),
#     path("medicalnotes/<int:pk>/", DetailMedicalNoteView.as_view()),
# ]
