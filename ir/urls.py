from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ir/', views.ir, name='imageRecognition')
]
