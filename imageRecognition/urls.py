from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from accounts import views as account_views 
import chat

urlpatterns = [
  url(r'^', include('chat.urls')),
  url(r'^login/', account_views.userLogin, name="userLogin"), 
  url(r'^logout/', account_views.userLogout, name="userLogout"), 
  url(r'^admin/', admin.site.urls),
]
