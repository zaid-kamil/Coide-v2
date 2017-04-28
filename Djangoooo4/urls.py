"""Djangoooo4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views
from poll.forms import LoginForm
from accounts.views import (login_view, logout_view, register_view)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('poll.urls')),
    url(r'^login/', login_view, name="login"),
    url(r'^logout/', logout_view, name="logout"),
    url(r'^register/', register_view, name="register"),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^search/', include('haystack.urls')),
    url(r'', include('codescript.urls'), name="save_scripts"),

]
# allow apps to upload files to the server
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
