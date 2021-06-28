
"""djangoProject URL Configuration

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
from django.contrib import admin
from django.urls import path, include

from administrater import views

urlpatterns = [
    path('login/',views.login,name='administrater_login'),
    path('home',views.home,name='administrater_home'),
    path('add_website_name',views.add_website_name,name='add_website_name'),
    path('add_website_menu',views.add_website_menu,name='add_website_menu'),
path('add_website_content',views.add_website_content,name='add_website_content'),
path('add_website_banner',views.add_website_banner,name='add_website_banner'),
path('add_website_footer',views.add_website_footer,name='add_website_footer'),
]
