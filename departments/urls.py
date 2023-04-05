from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('chief', views.DepartmentChiefView, basename='chief')

urlpatterns = [
    # department url
    path('', include(router.urls)),
    path('create-list/', views.department_list_create_view),
    path('update-delete/<int:pk>/', views.department_update_delete_view),
    
    # department program level url
    path('programlevel/create-list/', views.department_programlevel_list_create_view),
    path('programlevel/update-delete/<int:pk>/', views.department_programlevel_update_delete_view),
    
    # semester url
    path('semester/create-list/', views.semester_list_create_view),
    path('semester/update-delete/<int:pk>/', views.semester_update_delete_view),

    # subject url
    path('subject/create-list/', views.subject_list_create_view),
    path('subject/update-delete/<str:slug>/', views.subject_update_delete_view),
    
    
]