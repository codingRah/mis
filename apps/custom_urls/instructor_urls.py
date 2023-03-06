from django.urls import path,include
from apps.custom_views import instructor_views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('', instructor_views.InstructorViews,basename='instuctor')
router.register('cart', instructor_views.InstructorCart,basename='cart')
router.register('experience', instructor_views.InstructorExperience,basename='experience')
router.register('education', instructor_views.InstructorEducation,basename='education')
router.register('extraInfo', instructor_views.InstructorExtraInfo,basename='extraInfo')



urlpatterns = [
    path('', include(router.urls)),
]