"""
URL configuration for forDB project.

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
from django.urls import path
# urls.py

from django.urls import path
from postgre.views import index, allcolor_list, inventoryct_list, ord1_list, calendar_list

urlpatterns = [
    path('', index, name='index'),
    path('allcolors/', allcolor_list, name='allcolor_list'),
    path('inventorycts/', inventoryct_list, name='inventoryct_list'),
    path('ord1s/', ord1_list, name='ord1_list'),
    path('calendars/', calendar_list, name='calendar_list'),
    # path('my_view/', my_view, name='my_view'),  # 이 줄을 제거하거나 주석 처리하세요.


]
