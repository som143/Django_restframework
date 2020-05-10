"""django_restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from customers import views
from rest_framework.views import APIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/',views.customerAPiview.as_view()),
    path('customerdetail/<pk>/',views.customer_detail_api.as_view()),
    path('List_genericAPIview',views.customer_List_genericAPIview.as_view()),
    path('Detail_genericAPIview',views.customer_Detail_genericAPIview.as_view()),
    path('functionAPI',views.customer_functionAPI,name='customer_list'),
    path('funcn_detail_API/<pk>/',views.customer_detail_API),
    path('customer_deco_api',views.customer_deco_api),
    path('customer_detail_deco_api/<pk>/',views.customer_detail_deco_api),
]
