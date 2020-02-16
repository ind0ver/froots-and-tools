"""pyshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from products.views import *

urlpatterns = [
                  path('', broducts_view),
                  path('tools/', tools_view),
                  path('froots/', froots_view),
                  path('admin/', admin.site.urls),
                  path('broducts/', broducts_view),
                  path('contacts/', contacts_view),
                  path('search/', searchbar_view),
                  path('new/', new_view)] \
              + [*[path(f'broducts/{x}/', broducts_view) for x in range(1, 10)]] \
              + [*[path(f'froots/{x}/', froots_view) for x in range(1, 10)]] \
              + [*[path(f'tools/{x}/', tools_view) for x in range(1, 10)]] \
              + [*[path(f'search/{x}/', tools_view) for x in range(1, 10)]]
