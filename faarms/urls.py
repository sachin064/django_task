"""faarms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view


from students import views

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet,basename='studentship')

urlpatterns = [
    url(r'^openapi-schema',get_schema_view(title='farrms',version="3.0",public=True),name='openapi-schema'),
    url(r'docs/',TemplateView.as_view(template_name='swagger-ui.html',extra_context={'schema_url': 'openapi-schema'}
), name='swagger-ui'),
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]
