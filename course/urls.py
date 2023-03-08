from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("course", views.CourseViews, basename="course")
router.register("status", views.CourseStatusViews, basename="status")
router.register("detail", views.CourseDetailViews, basename="detail")

# router.register("status", StudentStatusViews, basename="status")
# router.register("contact", StudentRelationContactViews, basename="contact")
# router.register("hostel", StudentHostelViews, basename="hostel")
# router.register("cartinfo", StudentCartInfolViews, basename="cartinfo")



urlpatterns = [
    path('', include(router.urls)),
]