from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('instructor', views.InstructorViews, basename='instructor')
router.register('education', views.InstructorEducationViews, basename='education')
router.register('experience', views.InstructorExperience, basename='experience')
router.register('extrainfo', views.InstructorExtraInfo, basename='extrainformation')
router.register('cart', views.InstructorCartViews, basename='cart')


urlpatterns = [
    # department url
    path('', include(router.urls)),
    # path('education', views.InstructorEducationViews.as_view()),
]