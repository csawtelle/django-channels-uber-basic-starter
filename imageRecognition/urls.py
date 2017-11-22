from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from accounts import views as account_views 
import chat
import api
import rest_framework

urlpatterns = [
  url(r'^', include('chat.urls')),
  url(r'^admin/', admin.site.urls),
  url(r'^api/v1/auth/', include('rest_framework.urls', namespace='rest_framework')),
  url(r'^api/v1/', include('api.urls')),
]
