"""
URL configuration for todo project.

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
from django.urls import path, include
from drf_spectacular.views import (SpectacularAPIView,
                                   SpectacularRedocView,
                                   SpectacularSwaggerView,)
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView, 
                                            TokenRefreshView,
                                            TokenVerifyView,)

from tasks.views import TaskViewSet, RegisterAPIView, TaskAssignmentViewSet


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'task-assignments', TaskAssignmentViewSet, basename='task-assignment')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/register/", RegisterAPIView.as_view(), name="register"),
    path("api/v1/auth/", include("rest_framework.urls")),
    path('api/v1/', include(router.urls)),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # OpenAPI schema (JSON)
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    
    # Swagger UI
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    # ReDoc
    path('api/v1/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
