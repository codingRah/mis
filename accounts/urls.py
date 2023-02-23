from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.MyTokenObtainPairView.as_view()),
    path('list-create/', views.user_list_create_view),
    path('update-delete/<str:pk>/', views.user_update_delete_view),
    path('usertype/list-create/', views.usertype_list_create_view),
    path('usertype/update-delete/<str:pk>/', views.usertype_update_delete_view),
    path('permission/', views.permission_list_views),
    path('address/list-create/', views.useraddress_list_create_view),
    path('address/update-delete/<str:pk>/', views.useraddress_update_delete_view),
]