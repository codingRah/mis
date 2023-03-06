from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('student/', views.StudentViews, basename='student'),
router.register('status/', views.StudentStatusView, basename='status'),
router.register('hostel/', views.StudentHostelView, basename='hostel'),
router.register('contact/', views.StudentRelationContactView, basename='contact'),
router.register('cart/', views.StudentCartInfoView, basename='cart'),




urlpatterns = [
    path('', include(router.urls)),
]