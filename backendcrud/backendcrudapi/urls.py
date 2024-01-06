"""
URL configuration for backendcrud project.

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
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('get-csrf-token/', views.get_csrf_token, name='get_csrf_token'),
    path('signin/', views.user_login, name='user_login'),
    path('signup/', views.user_signup, name='user_signup'),
    path('add-customer/', views.CustomerList.as_view(), name='customerlist'),
    path('add-customer/<int:pk>/', views.CustomerDetail.as_view(), name='customerdetail'),
    path('delete-customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),
]
