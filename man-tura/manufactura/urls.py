"""manufactura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from manufactura.settings import dev 
from django.conf.urls.static import static

urlpatterns = [
    path('admin_panel/', admin.site.urls),
    path('restaurant_admin/', include('restaurant_admin.urls')),
    path('',include('mainpage.urls')),
    path('menu/', include('menu.urls')),
    path('order/', include('order.urls')),
    path('for_user/',include('for_user.urls'))
]

if  dev.DEBUG:
    # import debug_toolbar
    urlpatterns += static(dev.MEDIA_URL,document_root=dev.MEDIA_ROOT)
    urlpatterns += static(dev.STATIC_URL,document_root=dev.STATIC_URL)
    # urlpatterns = [
    #     path('__debug__/', include(debug_toolbar.urls)),
    # ] + urlpatterns
