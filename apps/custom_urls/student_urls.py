from django.urls import path,include
from apps.custom_views import student_views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('student/', student_views.StudentViews, basename='student'),
router.register('status/', student_views.StudentStatus, basename='status'),
router.register('hostel/', student_views.StudentHostel, basename='hostel'),




urlpatterns = [
    path('', include(router.urls)),
]