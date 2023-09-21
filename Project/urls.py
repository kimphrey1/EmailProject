"""
URL configuration for Project project.

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
from myApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('emaily/', include('emaily.urls')),  # Include the emaily app's URLs
    path('', views.home_view,),
    # path('send_email/', views.send_email, name='send_email'),
    # path('download_template/', views.download_excel_template, name='download_excel_template'),  # Add this URL pattern
]
