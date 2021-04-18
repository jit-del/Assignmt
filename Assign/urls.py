"""Assign URL Configuration

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
from app1 import views
from Assign import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='home.html'),name='home'),
    path('s_login/',views.slogin,name='s_login'),
    path('s_regitser/',views.s_regitser,name='s_regitser'),
    path('usucessregitser/',views.regitser,name='usucessregitser'),
    path('s_edit/',views.s_edit,name='s_edit'),
    path('s_logout/',views.s_logout,name='s_logout'),
    path('a_login/',views.a_login,name='a_login'),
    path('a_regitser/',views.a_regitser,name='a_regitser'),
    path('asucessregitser/',views.asucessregitser,name='asucessregitser'),
    path('a_logout/',views.a_logout,name='a_logout'),
    path('s_update/<int:pk>',views.s_update,name='s_update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)