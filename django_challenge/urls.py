"""django_challenge URL Configuration

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
from django.urls import include, path

# Alteração no painel administrativo
admin.site.site_header = "Administração"
admin.site.site_title = "ADM"
admin.site.index_title = "Bem vindo"

handler404 = 'apps.core.views.custom_404'
handler500 = 'apps.core.views.custom_500'
handler403 = "apps.core.views.custom_403"
handler400 = "apps.core.views.custom_400"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls', namespace='api')),
]
