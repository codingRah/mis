from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('result', views.ResultViews, basename='result')


urlpatterns = [
    path('', include(router.urls)),
    # path("upload/<str:pk>/", views.course_result_upload, name="upload")
        path("result-upload/", views.result_bulk_upload_view, name="result-upload"),

]
