from django.urls import path
from apps.custom_views import department_views

urlpatterns = [
    # department url
    path('department/create-list/', department_views.department_list_create_view),
    path('department/update-delete/<int:pk>/', department_views.department_update_delete_view),
    
    # department chief url
    path('chief/create-list/', department_views.department_chief_list_create_view),
    path('chief/update-delete/<int:pk>/', department_views.department_chief_update_delete_view),
    
    # department program level url
    path('programlevel/create-list/', department_views.department_programlevel_list_create_view),
    path('programlevel/update-delete/<int:pk>/', department_views.department_programlevel_update_delete_view),
    
    # semester url
    path('semester/create-list/', department_views.semester_list_create_view),
    path('semester/update-delete/<int:pk>/', department_views.semester_update_delete_view),


]