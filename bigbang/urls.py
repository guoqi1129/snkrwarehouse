"""bigbang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/',include('spaceship.urls_account',namespace="spaceship_account")),
    url(r'^form/',include('spaceship.urls_form',namespace="spaceship_form")),
    url(r'^table/',include('spaceship.urls_table',namespace="spaceship_table")),
    url(r'^main/',include('spaceship.urls_main',namespace="spaceship_main")),
    # path(r'login.html/', user_login),
    # path(r'index/', home_page),
    # path(r'index/warehouse_in.html', warehouse_in),
    # path(r'index/forms/bought.html', bought_new),
]
