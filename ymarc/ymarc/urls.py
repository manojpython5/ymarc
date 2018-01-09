"""ymarc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from ymarchome import views

app_name="ymarchome"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('ymarchome.urls')),
    url(r'^veg/',views.veg,name="veg"),
    url(r'^nonveg/',views.nonveg,name="nonveg"),
    url(r'^dairy/',views.dairy,name="dairy"),
    url(r'^registartion/',views.register,name="register"),
    url(r'^logout/',views.user_logout,name="logout"),
    url(r'^forgot_password/',views.forgot,name="forgot")
]
