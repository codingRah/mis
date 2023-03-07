from django.urls import path,include
from .views import StudentViews, StudentStatusViews, StudentRelationContactViews,StudentHostelViews, StudentCartInfolViews
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("student", StudentViews, basename="student")
router.register("status", StudentStatusViews, basename="status")
router.register("contact", StudentRelationContactViews, basename="contact")
router.register("hostel", StudentHostelViews, basename="hostel")
router.register("cartinfo", StudentCartInfolViews, basename="cartinfo")



urlpatterns = [
    path('', include(router.urls)),
]