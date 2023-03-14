from django.urls import path,include
from .views import StudentViews, StudentStatusViews,semester_report_view, student_bulk_upload_view, StudentRelationContactViews,StudentHostelViews, StudentCartInfolViews
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("student", StudentViews, basename="student")
router.register("status", StudentStatusViews, basename="status")
router.register("contact", StudentRelationContactViews, basename="contact")
router.register("hostel", StudentHostelViews, basename="hostel")
router.register("cartinfo", StudentCartInfolViews, basename="cartinfo")



urlpatterns = [
    path('', include(router.urls)),
    path("upload/" , student_bulk_upload_view, name="upload"),
    path("report/<str:pk>/" , semester_report_view, name="report")
]