from django.urls import path
from . import views

urlpatterns = [
    # department url
    path('department/create-list/', views.department_list_create_view),
    path('department/update-delete/<int:pk>/', views.department_update_delete_view),
    
    # department chief url
    path('chief/create-list/', views.department_chief_list_create_view),
    path('chief/update-delete/<int:pk>/', views.department_chief_update_delete_view),
    
    # department program level url
    path('programlevel/create-list/', views.department_programlevel_list_create_view),
    path('programlevel/update-delete/<int:pk>/', views.department_programlevel_update_delete_view),
    
    # semester url
    path('semester/create-list/', views.semester_list_create_view),
    path('semester/update-delete/<int:pk>/', views.semester_update_delete_view),
    
    
]