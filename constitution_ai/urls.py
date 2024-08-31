"""
URL configuration for constitution_ai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
import aid_bot.views as ab
from traffic.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aid_bot/', ab.page, name='aid_bot'),
    path('aid_bot/chat/', ab.chatbot_response, name='chatbot_response'),
    path('', home, name='home')
]
