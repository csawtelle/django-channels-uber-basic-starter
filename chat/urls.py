from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ir, name='ir'),
    url(r'^chat/send', views.sendMessage, name='send'),
    url(r'^chat/receive', views.receiveMessage, name='receive'),
]
