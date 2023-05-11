"""
URL configuration for rateMyPaste project.

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
from django.contrib.auth import views as auth_views

from web import views as web_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', web_views.home, name='home'),
    path('register/', web_views.register, name='register'),

    path('login/', auth_views.LoginView.as_view(template_name='web/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='web/logout.html'), name='logout'),
    path('pokemon/create/', web_views.pokemon_create, name='pokemon_create'),
    path('pokemon/<int:pk>/edit/', web_views.pokemon_edit, name='pokemon_edit'),
    path('pokemon/<int:pk>/delete/', web_views.pokemon_delete, name='pokemon_delete'),
    path('pokemon/<int:pk>/', web_views.pokemon_detail, name='pokemon_detail'),
    path('pokemon/', web_views.pokemon_list, name='pokemon_list'),
    path('paste/', web_views.paste_list, name='paste_list'),
    path('paste/create/', web_views.paste_create, name='paste_create'),
    path('paste/<int:pk>/edit/', web_views.paste_edit, name='paste_edit'),
    path('paste/<int:pk>/delete/', web_views.paste_delete, name='paste_delete'),
    path('paste/<int:pk>/', web_views.paste_detail, name='paste_detail'),

]
