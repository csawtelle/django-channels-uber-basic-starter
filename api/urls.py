from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import api_chat

app_name = 'api'

urlpatterns = [
  url(r'^conversations/$', api_chat.ConversationsList.as_view(), name="conversations_api"),
  url(r'^messages/$', api_chat.MessagesList.as_view(), name="messages_api"),
]
