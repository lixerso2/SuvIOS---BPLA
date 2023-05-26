
"""
URL configuration for suvios_bpla project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import suvios.urls
from django.conf.urls.static import static
from suvios.views import ApiEndpoint
from oidc_provider.views import ProviderInfoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello', ApiEndpoint.as_view()),
    path('', include('suvios.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('.well-known/openid-configuration', ProviderInfoView.as_view()),
    path('openid/', include('oidc_provider.urls', namespace='oidc_provider')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

