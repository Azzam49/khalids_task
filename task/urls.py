"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django_rest_passwordreset.views import (
    reset_password_validate_token,
    reset_password_confirm,
    reset_password_request_token,
)

urlpatterns = [
    path('admin/', admin.site.urls),
]

# app urls
urlpatterns += [
    path('api/', include('task.app.urls')),
]

# for JWT token
urlpatterns += [
    path('api/token-auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# for password rest
urlpatterns += [
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]