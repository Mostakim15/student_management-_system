"""
URL configuration for exam_pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include 
from django.conf import settings
from django.conf.urls.static import static
# This is the main URL configuration for the exam_pro project.


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exam_app.urls')),  # Home application
    path('edit/', include('edit_app.urls')),  # Edit application
    path('delete/', include('delete_app.urls')),  # Delete application
    path('create/', include('create_app.urls')),  # Create application
]

if settings.DEBUG:
    # Serve static files during development
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Serve media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)