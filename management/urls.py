from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("auth/", include("djoser.urls.jwt")),
    path('user/', include('accounts.urls')),
    path('department/', include('departments.urls')),
    path('student/', include('students.urls')),
    path('instructor/', include('staff.urls')),
    path('course/', include('course.urls')),
    path('result/', include('results.urls')),
    path('task/', include('tasks.urls')),
    path('schedule/', include('schedule.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
