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
    path('apps/', include('apps.custom_urls.department_urls')),
    path('instructor/', include('apps.custom_urls.instructor_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
