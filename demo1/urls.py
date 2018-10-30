from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import login

from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]