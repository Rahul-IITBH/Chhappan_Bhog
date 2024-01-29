"""
URL configuration for Chhappan_Bhog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from customer import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('login/', LoginView.as_view(template_name='customer/login.html'), name='login'),
    path('signup/', views.signup,  name = 'signup'),
    path('dashboard/', views.dashboard,  name = 'dashboard'),
    path('restaurant_registration/', views.restaurant_registration,  name = 'restaurant_registration'),
    path('restaurant_login/', views.restaurant_login,  name = 'restaurant_login'),
    path('restaurant_dashboard/', views.restaurant_dashboard,  name = 'restaurant_dashboard'),
    path('delivery_login/', LoginView.as_view(template_name='delivery_partner/delivery_login.html'), name='delivery_login'),
    path('delivery_signup/', views.delivery_signup,  name = 'delivery_signup'),
    path('delivery_dashboard/', views.delivery_dashboard,  name = 'delivery_dashboard'),
]
