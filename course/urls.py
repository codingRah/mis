from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("course", views.CourseViews, basename="course")
router.register("status", views.CourseStatusViews, basename="status")
router.register("detail", views.CourseDetailViews, basename="detail")
router.register("module", views.CourseModuleViews, basename="module")
router.register("contenttype", views.CourseContentTypeViews, basename="contenttype")

router.register("event", views.CourseEventViews, basename="event")
# router.register("contact", StudentRelationContactViews, basename="contact")
# router.register("hostel", StudentHostelViews, basename="hostel")
# router.register("cartinfo", StudentCartInfolViews, basename="cartinfo")



urlpatterns = [
    path('', include(router.urls)),
]