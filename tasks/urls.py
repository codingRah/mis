from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('assignment', views.AssignmentViews, basename='assignment')


urlpatterns = [
    # assignment url
    path('', include(router.urls)),
]