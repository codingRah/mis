from django.urls import path,include
from apps.custom_views import student_views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('', student_views.StudentViews, basename='student')
router.register('status/', student_views.StudentStatus, basename='status')
router.register('hostel/', student_views.StudentHostel, basename='hostel')
router.register('relationcontact/', student_views.StudentRelationContactView, basename='relationcontact')
router.register('cartinfo/', student_views.StudentCartInfoView, basename='cartinfo')




urlpatterns = [
    path('', include(router.urls)),
]