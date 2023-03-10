from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("course", views.CourseViews, basename="course")
router.register("status", views.CourseStatusViews, basename="status")
router.register("detail", views.CourseDetailViews, basename="detail")
router.register("module", views.CourseModuleViews, basename="module")
router.register("contenttype", views.CourseContentTypeViews, basename="contenttype")
router.register("session", views.CourseSessionViews, basename="session")


router.register("event", views.CourseEventViews, basename="event")
router.register("content", views.CourseContentViews, basename="content")
router.register("subject-assign", views.SubjectAssignmentToInstructorViews, basename="subject-assign")


urlpatterns = [
    path('', include(router.urls)),
]